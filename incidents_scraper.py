from bs4 import BeautifulSoup
import requests

from data import incidents_soup_broth as broth
from data import incidents_soup_ingredients as ingr

def scrape_incidents():
    incidents_list = cook_soup()
    return incidents_list

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
                if(table_columns[0].text == ingr[i][1]):
                    new_entry = []
                    new_entry.append(ingr[i][0])
                    new_entry.append(table_columns[5].text.replace(",", "."))
                    incidents_list.append(new_entry)
    return incidents_list