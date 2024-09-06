from bs4 import BeautifulSoup
import requests
import time
import codecs
import threading

TIMEOUT = 3

from data import weather_descriptions as wd

def scrape_weather():
    temp, desc = cook_weather_soup()
    sunrise_str, sunset_str = cook_daylight_soup()
    if(temp == None):
        return None
    update_descriptions(desc)
    img_name = None
    if(get_description_index(desc) != None):
        img_name = get_daytime_index(sunrise_str, sunset_str) + get_description_index(desc) + ".png"
    return [temp, img_name, sunrise_str, sunset_str]

def set_timeout(event):
    event.set()

def cook_weather_soup():
    req = None
    event = threading.Event()
    timer = threading.Timer(TIMEOUT, set_timeout, [event])

    timer.start()
    while(req == None and not event.is_set()):
        try:
            req = requests.get("https://weather.com/de-DE/wetter/heute/l/3a290f5daf6568a77c79271dc2aa5fb217ceab85a1ba3c54c8d16efac932edfb")
        except:
            return None, None
    soup = BeautifulSoup(req.text, "lxml")
    try:
        current_temp_str = get_current_temperature(soup)
        night_temp_str = get_night_temperature(soup)
        current_desc_str = get_current_description(soup)
    except:
        return None, None
    return [current_temp_str + " / " + night_temp_str, current_desc_str]

def cook_daylight_soup():
    req = None
    try:
        req = requests.get("https://www.timeanddate.com/sun/germany/erlangen")
    except:
        return None, None
    soup = BeautifulSoup(req.text, "lxml")

    container_list = soup.find_all("tr")
    sunrise_str = container_list[5].find("td").text[0:5]
    sunset_str = container_list[6].find("td").text[0:5]
    return [sunrise_str, sunset_str]

def get_current_temperature(soup):
    class_names =   [
                        "CurrentConditions--tempValue--MHmYY",
                        "CurrentConditions--tempValue--3a50n",
                        "CurrentConditions--tempValue--1RYJJ",
                        "CurrentConditions--tempValue--3KcTQ"
                    ]
    span = None
    for class_name in class_names:
        span = soup.find("span", class_=class_name)
        if(span != None):
            break
    return span.text

def get_night_temperature(soup):
    class_names =   [
                        "CurrentConditions--tempHiLoValue--3T1DG",
                        "CurrentConditions--tempHiLoValue--3T1DG",
                        "CurrentConditions--tempHiLoValue--3SUHy",
                        "CurrentConditions--tempHiLoValue--1s05u",
                        "CurrentConditions--tempHiLoValue--A4RQE"
                    ]
    div = None
    for class_name in class_names:
        div = soup.find("div", class_=class_name)
        if(div != None):
            break
    return div.find_all("span")[2].text

def get_current_description(soup):
    class_names =   [
                        "CurrentConditions--phraseValue--mZC_p",
                        "CurrentConditions--phraseValue--2Z18W",
                        "CurrentConditions--phraseValue--17s79",
                        "CurrentConditions--phraseValue--2xXSr"
                    ]
    desc = None
    for class_name in class_names:
        desc = soup.find("div", class_=class_name)
        if(desc != None):
            break
    return remove_secondary_descriptions(desc.text)

def remove_secondary_descriptions(description):
    for i in range(len(description)):
        if(description[i] == "/"):
            return description[0:i]
    return description

def update_descriptions(desc_str):
    desc_file, desc_text = get_desc_file(desc_str)
    if(desc_file != None):
        desc_file.write(desc_text + desc_str + "\n")
    
def get_desc_file(desc_str):
    desc_list, desc_text = get_known_descriptions()
    is_unique = True
    for entry in desc_list:
        if(entry == desc_str):
            is_unique = False
            break
    if(is_unique):
        return codecs.open("weather/descriptions.txt", "w", "utf-8"), desc_text
    return None, None

def get_known_descriptions():
    desc_file = codecs.open("weather/descriptions.txt", "r", "utf-8")
    desc_text = desc_file.read()
    desc_list = desc_text.split("\n")
    return desc_list, desc_text

def get_daytime_index(sunrise_str, sunset_str):
    date = get_date()
    hour = date.tm_hour
    minute = date.tm_min
    sunrise_hour, sunrise_minute = get_hour_and_min(sunrise_str)
    sunset_hour, sunset_minute = get_hour_and_min(sunset_str)
    if(hour > sunrise_hour and (hour < sunset_hour or (hour == sunset_hour and minute < sunset_minute))):
        return "0"
    elif(hour == sunrise_hour and (minute >= sunrise_minute)):
        return "0"
    return "1"

def get_hour_and_min(time_str):
    time_list = time_str.split(":")
    return int(time_list[0]), int(time_list[1])

def get_description_index(desc):
    for i in range(len(wd)):
        for string in wd[i]:
            if(desc == string):
                return str(i)
    return None

def get_date():
    return time.localtime(time.time())

cook_daylight_soup()