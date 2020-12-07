import os
import ctypes
import time

import image_design as dsgn
import birthday_scraper as bs
import finance_scraper as fs
import news_scraper as ns
import weather_scraper as ws
import change_wallpaper as cw
import output as op

DAY_OFFSET = 0
IMG_PATH = "C:/Users/tkroe/Desktop/Python/Smart_Wallpaper/"
IMG_NAME = "current_img.png"
IMG_NAME_NEW = "new_img.png"
IMG_NAME_PREV = "previous_img.png"

def the_one_ring():
    op.heading()
    try:
        os.remove(IMG_PATH + IMG_NAME)
    except:
        pass
    img = dsgn.create_raw_image(DAY_OFFSET)
    img = draw_calendar(img, DAY_OFFSET)
    img = scrape_n_draw_birthday_info(img, DAY_OFFSET)
    img = scrape_n_draw_finances(img, DAY_OFFSET)
    img = scrape_n_draw_news(img)
    img = scrape_n_draw_weather(img)

    cw.save_img(img, IMG_NAME_NEW)
    cw.change_wallpaper(IMG_PATH + IMG_NAME_NEW)
    os.rename(IMG_NAME_NEW, IMG_NAME)

    op.final_words()

def draw_calendar(img, added_days):
    todo_list = []
    if(bs.get_date(added_days).tm_wday == 5):
        todo_list.append("Mama anrufen")
    if(len(todo_list) != 0):
        img = dsgn.draw_calendar_widgets(img, todo_list)
    return img
    

def scrape_n_draw_birthday_info(img, added_days):
    op.birthday_intro()
    todays_list, num_events_today = bs.get_daily_reminders(added_days)
    months_list = bs.get_monthly_reminders(added_days)
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

the_one_ring()