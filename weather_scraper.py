from bs4 import BeautifulSoup
import requests
import time
import codecs

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

def cook_weather_soup():
    req = None
    try:
        req = requests.get("https://weather.com/de-DE/wetter/heute/l/adaf6ffddd7b1048f3e96218716384fb87b7ce06115f583819dc1196e34b577c")
    except:
        return None, None
    soup = BeautifulSoup(req.text, "lxml")

    current_temp_str = get_current_temperature(soup)
    night_temp_str = get_night_temperature(soup)
    current_desc_str = get_current_description(soup)
    return [current_temp_str + " / " + night_temp_str, current_desc_str]

def cook_daylight_soup():
    req = None
    try:
        req = requests.get("https://www.timeanddate.com/sun/germany/augsburg")
    except:
        return None, None
    soup = BeautifulSoup(req.text, "lxml")

    container_list = soup.find_all("tr")
    sunrise_str = container_list[5].find("td").text[0:5]
    sunset_str = container_list[6].find("td").text[0:5]
    return [sunrise_str, sunset_str]

def get_current_temperature(soup):
    return soup.find("span", class_="CurrentConditions--tempValue--3KcTQ").text

def get_night_temperature(soup):
    div = soup.find("div", class_="CurrentConditions--tempHiLoValue--A4RQE")
    return div.find_all("span")[1].text

def get_current_description(soup):
    return soup.find("div", class_="CurrentConditions--phraseValue--2xXSr").text

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
        return open("weather/descriptions.txt", "w"), desc_text
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