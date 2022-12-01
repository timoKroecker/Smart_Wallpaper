import time

from data import weekdays
import database_interface as dbi

def scrape_university(added_days):
    dbi.create_university_tables()

    todays_list, num_events_today = get_daily_reminders(added_days)
    tomorrows_list = get_tomorrow_reminders(added_days)

    return [todays_list, num_events_today, tomorrows_list]

def get_daily_reminders(added_days):
    date = get_date(added_days)
    output = []
    num_events = 0
    university_list = dbi.select_university_by_weekday(str(date.tm_wday))
    for elem in university_list:
        output.append([elem[0], elem[2], elem[3], elem[4], elem[5]])
        num_events = num_events + 1
    return output, num_events

def get_tomorrow_reminders(added_days):
    output= []
    date = get_date(added_days + 1)
    university_list = dbi.select_university_by_weekday(str(((date.tm_wday % 7) % 6) % 5))
    for elem in university_list:
        output.append([elem[0], elem[2], elem[3], elem[4], elem[5]])
    return output

def get_date(added_days):
    return time.localtime(time.time() + added_days * 86400)