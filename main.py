import os
import ctypes
import time
import codecs

import image_design as dsgn
import birthday_scraper as bs
import finance_scraper as fs
import news_scraper as ns
import weather_scraper as ws
import change_wallpaper as cw
import output as op

DAY_OFFSET = 0
PATH = os.path.dirname(os.path.realpath(__file__))
IMG_NAME = "current_img.png"

def the_one_ring():
    op.heading()
    try:
        os.remove(PATH + IMG_NAME)
    except:
        pass
    settings = collect_settings()
    img = dsgn.create_raw_image(DAY_OFFSET)
    img = scrape_n_draw_birthday_info(img, DAY_OFFSET)
    img = scrape_n_draw_finances(img, DAY_OFFSET)
    img = scrape_n_draw_news(img)
    img = scrape_n_draw_weather(img)

    cw.save_img(img, IMG_NAME)
    cw.change_wallpaper(PATH + "/" + IMG_NAME, settings[0])

    op.final_words()

def scrape_n_draw_birthday_info(img, added_days):
    op.birthday_intro()

    birthdays_list = bs.scrape_birthdays(added_days)
    todays_list = birthdays_list[0]
    num_events_today = birthdays_list[1]
    months_list = birthdays_list[2]

    if(len(todays_list) != 0 or len(months_list) != 0):
        img = dsgn.draw_birthday_widgets(img, todays_list, num_events_today, months_list)
        op.visible()
    else:
        op.hidden()
    return img

def scrape_n_draw_finances(img, added_days):
    op.finance_intro()
    finances = fs.scrape_finances(added_days)
    month_expences = finances[0][0]
    month_total = finances[0][1]
    month_str = finances[0][2]
    year_expences = finances[1][0]
    year_total = finances[1][1]
    year_str = finances[1][2]
    year_expences, year_total, year_str = fs.get_years_expences(added_days)
    if(True):
        img = dsgn.draw_finance_widgets(    img,
                                            month_expences,
                                            month_total,
                                            month_str,
                                            year_expences,
                                            year_total,
                                            year_str)
        op.visible()
    else:
        op.hidden()
    return img

def scrape_n_draw_news(img):
    op.news_intro()
    headline_list = ns.scrape_news_headlines()
    if(headline_list != None):
        dsgn.draw_news_widgets(img, headline_list)
        op.visible()
    else:
        op.hidden()
    return img

def scrape_n_draw_weather(img):
    op.weather_intro()
    weather_list = ws.scrape_weather()
    if(weather_list != None):
        img = dsgn.draw_weather_widgets(img, weather_list)
        op.visible()
    else:
        op.hidden()
    return img

def collect_settings():
    settings_file = open(PATH + "/settings.txt", "r")
    temp_settings_list = settings_file.read().split("\n")
    temp_settings_list_two = []
    for string in temp_settings_list:
        if(string != ""):
            temp_settings_list_two.append(string.split("\t"))
    final_settings_list = []
    for entry in temp_settings_list_two:
        try:
            final_settings_list.append(int(entry[1]))
        except:
            final_settings_list.append(entry[1])
    return final_settings_list

the_one_ring()