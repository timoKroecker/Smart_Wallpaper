from bs4 import BeautifulSoup
import requests
import threading
from datetime import datetime
import time

import database_interface as dbi

TIMEOUT = 3

FLAG_RETURNED_TODAY = "Heute zurückgegeben"
FLAG_AVAILABLE = "Verfügbar"
FLAG_BORROWED = "Entliehen"
FLAG_RESERVED = "Zurückgelegt"
FLAG_LOCKED = "Gesperrt"
FLAG_ORDERED = "Bestellt"
FLAG_IN_PROGRESS = "in Bearbeitung"
FLAG_VALID_STORE = "Hauptstelle"

def scrape_library():
    dbi.create_library_tables()

    library = dbi.select_all_library()
    soups = cook_all_soups(library)
    returned_today = get_returned_today(soups)
    available = get_available(soups)
    unavailable = get_unavailable(soups)

    return returned_today, available, unavailable

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

def get_unavailable(soups):
    """
    Returns all borrowed and reserved items
    sorted by number of reservations and deadline.
    """
    unavailable = []
    for soup in soups:
        name = soup[0]
        medium = soup[1]
        status = soup[2]
        deadline = soup[3]
        num_reservations = soup[4]
        if (status == FLAG_BORROWED or
            status == FLAG_RESERVED):
            unavailable.append([name, medium, deadline, num_reservations])
    return sort_unavailable(unavailable)

def sort_reserved(reserved):
    return sorted(reserved, key=lambda x: x[2])

def sort_unavailable(borrowed):
    return sorted(borrowed, key=lambda x: (x[3], datetime.strptime(get_valid_date(x[2]), "%d.%m.%Y")))

def sort_raw(raw):
    status_to_order = {
                        FLAG_RETURNED_TODAY: 0,
                        FLAG_AVAILABLE: 1,
                        FLAG_BORROWED: 2,
                        FLAG_RESERVED: 2,
                        FLAG_LOCKED: 99,
                        FLAG_ORDERED: 99,
                        FLAG_IN_PROGRESS: 99
                      }
    return sorted(raw,
                  key=lambda x: (status_to_order[x[0]],
                                 x[2],
                                 datetime.strptime(get_valid_date(x[1]), "%d.%m.%Y")))

def get_valid_date(date_str):
    if(date_str == ""):
        return "01.01.0001"
    return date_str

def is_deadline_past(deadline):
    if deadline == "":
        return False
    deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
    today_date = datetime.strptime(get_localdate(), "%d.%m.%Y")
    if today_date < deadline_date:
        return False
    return True

def cook_all_soups(library):
    all_soups = []
    for library_entry in library:
        link = library_entry[2]
        soup = cook_soup(link)
        if not soup == None:
            all_soups.append(soup)
    return all_soups

def set_timeout(event):
    event.set()

def cook_soup(link):
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
    
    name = cook_name(soup)
    medium = cook_medium(soup)

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

    sorted_soups = sort_raw(soups)
    for soup in sorted_soups:
        if(not is_deadline_past(soup[1])):
            return [name, medium] + soup
    return None

def cook_name(soup):
    return soup.find("h3", class_="oclc-override-heading").text

def cook_medium(soup):
    abreviations =  {
                        "Buch Romane": "Buch",
                        "DVD": "DVD",
                        "Blu-ray": "BluRay",
                        "Sachbücher": "Buch",
                        "Jugendroman": "Buch"
                    }
    text = soup.find("span",
                     id=("dnn_ctr378_MainView_UcDetailView_uc" +
                         "SharedCatalogueView_spanMediaGrpValue")).text
    text = text.replace("\r", "").replace("\n", "").replace("\t", "")
    return abreviations[text]

def get_localdate():
    time_ = time.localtime(time.time())
    day = time_.tm_mday
    mon = time_.tm_mon
    year = time_.tm_year
    return str(day) + "." + str(mon) + "." + str(year)