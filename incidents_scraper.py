from bs4 import BeautifulSoup
import requests
import time

import database_interface as dbi

from data import incidents_soup_broth as broth
from data import incidents_soup_ingredients as ingr

def scrape_incidents():
    dbi.create_incidents_tables()
    incidents_list = cook_soup()
    incidents_plot_cube = dbi.select_incidents_plot_cube()
    if(incidents_list == None):
        incidents_list = dbi.select_incidents_by_date(get_localtime(0))
        if(len(incidents_list) == 0): return None, None
        return reformat_incidents_selection(incidents_list), incidents_plot_cube
    update_database(incidents_list)
    return incidents_list, incidents_plot_cube

def cook_soup():
    req = None
    try:
        req = requests.get(broth)
    except:
        return None

    soup = BeautifulSoup(req.text, 'lxml')
    #check if the html text is just a blank header
    if(len(str(soup)) < 5000):
        return None
    table = soup.find("table", id="tableLandkreise")
    table_rows = table.find_all("tr")
    
    incidents_list = []
    for i in range(len(ingr)):
        for j in range(len(table_rows)):
            table_columns = table_rows[j].find_all("td")
            if(len(table_columns) > 0):
                if(trim_string(table_columns[0].text) == ingr[i][1]):
                    new_entry = []
                    new_entry.append(ingr[i][0])
                    trimmed_incidence = trim_string(table_columns[5].text)
                    new_entry.append(trimmed_incidence)
                    incidents_list.append(new_entry)
    return incidents_list

def trim_string(string):
    string = string.replace("\r", "")
    string = string.replace("\n", "")
    string = string.replace(" ", "")
    string = string.replace(",", ".")
    return string

def update_database(incidents_list):
    date = get_localtime(0)
    day_str = str(date.tm_mday)
    month_str = str(date.tm_mon)
    year_str = str(date.tm_year)
    if(incidents_list == None): return
    if(len(dbi.select_incidents_by_date(date)) == 0):
        for array in incidents_list:
            dbi.insert_into_incidents(array[0], day_str, month_str, year_str, array[1])
    else:
        for array in incidents_list:
            dbi.update_incidents(array[0], day_str, month_str, year_str, array[1])

def reformat_incidents_selection(incidents_list):
    list_reformatted = []
    for row in incidents_list:
        row_reformatted = []
        row_reformatted.append(str(row[0]))
        row_reformatted.append(str(row[1]))
        list_reformatted.append(row_reformatted)
    return list_reformatted

def get_localtime(added_days):
    return time.localtime(time.time() + added_days * 86400)