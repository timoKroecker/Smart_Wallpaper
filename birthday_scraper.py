import time

import data as da
from data import birthdays_categories as bc
from data import text_file_header as header
import database_interface as dbi

def scrape_birthdays(added_days):
    dbi.create_birthday_tables()

    todays_list, num_events_today = get_daily_reminders(added_days)
    months_list = get_monthly_reminders(added_days)
    return [todays_list, num_events_today, months_list]

def get_daily_reminders(added_days):
    date = get_date(added_days)
    output = []
    num_events = 0
    birthdays_list = dbi.select_birthdays_by_date(str(date.tm_mday), str(date.tm_mon))
    for item in birthdays_list:
        num_events = num_events + 1
        entry = []
        entry.append(item[0])
        if(int(item[3]) != 0):
            entry.append(str(date.tm_year - int(item[3])))
        else:
            entry.append("")
        output.append(entry)
    return output, num_events

def get_monthly_reminders(added_days):
    output= []
    for i in range(31):
        date = get_date(added_days + i + 1)
        birthdays_list = dbi.select_birthdays_by_date(str(date.tm_mday), str(date.tm_mon))
        for item in birthdays_list:
            output.append(get_dated_reminder(date, item[0], added_days))
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
        output.append(da.weekdays[date.tm_wday][0])
    output.append(caption)
    return output

def get_time_string(added_days):
    date = get_date(added_days)
    string =    (da.weekdays[date.tm_wday][1] + "   " +
                str(date.tm_mday) + "." +
                str(date.tm_mon) + "." +
                str(date.tm_year) + "   " +
                str(date.tm_hour) + ":")
    if(date.tm_min < 10):
        return string + "0" + str(date.tm_min)
    return string + str(date.tm_min)

def get_date(added_days):
    return time.localtime(time.time() + added_days * 86400)