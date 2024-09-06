from bs4 import BeautifulSoup
import requests
import re
import threading
from datetime import datetime

import database_interface as dbi

TIMEOUT = 3

FLAG_RETURNED_TODAY = "Heute zurückgegeben"
FLAG_AVAILABLE = "Verfügbar"
FLAG_BORROWED = "Entliehen"
FLAG_RESERVED = "Vorbestellt"
FLAG_VALID_STORE = "Hauptstelle"

def scrape_library():
    dbi.create_library_tables()

    library = dbi.select_all_library()
    soups = cook_all_soups(library)
    returned_today = get_returned_today(soups)
    available = get_available(soups)
    reserved = get_reserved(soups)
    borrowed = get_borrowed(soups)

    return returned_today, available, reserved, borrowed

def get_returned_today(soups):
    returned_today = []
    for soup in soups:
        name = soup[0]
        medium = soup[1]
        status = soup[2]
        if status == FLAG_RETURNED_TODAY:
            returned_today.append([name, medium])
    return returned_today

def get_available(soups):
    available = []
    for soup in soups:
        name = soup[0]
        medium = soup[1]
        status = soup[2]
        if status == FLAG_AVAILABLE:
            available.append([name, medium])
    return available

def get_reserved(soups):
    reserved = []
    for soup in soups:
        name = soup[0]
        medium = soup[1]
        status = soup[2]
        num_reservations = soup[4]
        if status == FLAG_RESERVED:
            reserved.append([name, medium, num_reservations])
    return sorted(reserved, key=lambda x: x[2])

def get_borrowed(soups):
    """
    Returns all borrowed items
    sorted by number of reservations and deadline.
    """
    borrowed = []
    for soup in soups:
        name = soup[0]
        medium = soup[1]
        status = soup[2]
        deadline = soup[3]
        num_reservations = soup[4]
        if status == FLAG_BORROWED:
            borrowed.append([name, medium, deadline, num_reservations])
    return sorted(borrowed, key=lambda x: (x[3], datetime.strptime(x[2], "%d.%m.%Y")))

def cook_all_soups(library):
    all_soups = []
    for library_entry in library:
        link = library_entry[2]
        some_soups = cook_soups(link)
        for soup in some_soups:
            all_soups.append(list(library_entry)[:-1] + soup)
    return all_soups

def set_timeout(event):
    event.set()

def cook_soups(link):
    req = None
    event = threading.Event()
    timer = threading.Timer(TIMEOUT, set_timeout, [event])
    
    timer.start()
    while(req == None and not event.is_set()):
        try:
            req = requests.get(link)
        except:
            return None
    soup = BeautifulSoup(req.text, 'lxml')
    #check if the html text is just a blank header
    if(len(str(soup)) < 5000):
        return None
    td = soup.find_all("td", style="")
    matches = []
    for widget in td:
        matches += widget.find_all("span")

    soups = []
    for i in range(0, len(matches), 10):
        status = matches[i + 3].text
        deadline = matches[i + 5].text
        num_reservations = int(matches[i + 7].text)
        store = matches[i + 9].text
        if store == FLAG_VALID_STORE:
            soups.append([status, deadline, num_reservations])
    return soups