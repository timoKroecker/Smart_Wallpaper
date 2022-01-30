import os

import image_design_2 as dsgn
import calendar_scraper as cs
import birthday_scraper as bs
import finance_scraper as fs
import news_scraper as ns
import weather_scraper as ws
import incidents_scraper as ins
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
    img = dsgn.create_raw_image(DAY_OFFSET)
    img = scrape_n_draw_calendar(img, DAY_OFFSET)
    img = scrape_n_draw_birthday_info(img, DAY_OFFSET)
    img = scrape_n_draw_finances(img, DAY_OFFSET)
    img = scrape_n_draw_news(img)
    img = scrape_n_draw_weather(img)
    img = scrape_n_draw_incidents(img)

    cw.save_img(img, IMG_NAME)
    cw.change_wallpaper(PATH + "/" + IMG_NAME)

    op.final_words()

def scrape_n_draw_calendar(img, added_days):
    op.calendar_intro()

    calendar_list = cs.scrape_calendar(added_days)
    todays_list = calendar_list[0]
    num_events_today = calendar_list[1]
    months_list = calendar_list[2]
    
    if(len(todays_list) != 0 or len(months_list) != 0):
        img = dsgn.draw_calendar_widgets(img, todays_list, num_events_today, months_list)
        op.visible()
    else:
        op.hidden()
    return img

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
    op.expenditure_intro()
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

def scrape_n_draw_incidents(img):
    op.incidents_intro()
    incidents_list, incidents_plot_cube = ins.scrape_incidents()
    if(incidents_list != None):
        img = dsgn.draw_incidents_widgets(img, incidents_list, incidents_plot_cube)
        op.visible()
    else:
        op.hidden()
    return img

the_one_ring()