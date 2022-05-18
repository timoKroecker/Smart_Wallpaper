import time

from data import weekdays
import database_interface as dbi

def scrape_university(added_days):
    dbi.create_university_tables()

    todays_list, num_events_today = get_daily_reminders(added_days)
    week_list = get_weekly_reminders(added_days)

    return [todays_list, num_events_today, week_list]

def get_daily_reminders(added_days):
    date = get_date(added_days)
    output = []
    num_events = 0
    university_list = dbi.select_university_by_date(str(date.tm_mday), str(date.tm_mon), str(date.tm_year))
    for elem in university_list:
        output.append(elem[0])
        num_events = num_events + 1
    return output, num_events

def get_weekly_reminders(added_days):
    output= []
    for i in range(7):
        date = get_date(added_days + i + 1)
        university_list = dbi.select_university_by_date(str(date.tm_mday), str(date.tm_mon), str(date.tm_year))
        for elem in university_list:
            output.append(get_dated_reminder(date, elem[0], added_days))
    return output

def get_dated_reminder(date, caption, added_days):
    output = []
    if(date.tm_yday - 1 == get_date(added_days).tm_yday):
        output.append("morgen")
        output.append("")
    elif(date.tm_yday - 2 == get_date(added_days).tm_yday):
        output.append("übermorgen")
        output.append("")
    else:
        date_string = ""
        if(date.tm_mday < 10):
            date_string = date_string + "0"
        date_string = date_string + str(date.tm_mday) + "."
        if(date.tm_mon < 10):
            date_string = date_string + "0"
        date_string = date_string + str(date.tm_mon) + "."
        output.append(date_string)
        output.append(weekdays[date.tm_wday][0])
    output.append(caption)
    return output

def get_date(added_days):
    return time.localtime(time.time() + added_days * 86400)