import time

from data import weekdays

import database_interface as dbi

def scrape_calendar(added_days):
    dbi.create_calendar_tables()

    todays_list, num_events_today = get_daily_reminders(added_days)
    months_list = get_two_weeks_reminders(added_days)

    return [todays_list, num_events_today, months_list]

def get_daily_reminders(added_days):
    date = get_date(added_days)
    output = []
    num_events = 0
    if(is_mothersday(date)):
        num_events = num_events + 1
        output.append("Muttertag")
    if(is_fathersday(date)):
        num_events = num_events + 1
        output.append("Vatertag")
    calendar_list = dbi.select_calendar_by_date(str(date.tm_mday), str(date.tm_mon), str(date.tm_year))
    for elem in calendar_list:
        output.append(elem[0])
        num_events = num_events + 1
    return output, num_events

def get_two_weeks_reminders(added_days):
    output= []
    for i in range(31):
        date = get_date(added_days + i + 1)
        if(is_mothersday(date)):
            output.append(get_dated_reminder(date, "Muttertag", added_days))
        if(is_fathersday(date)):
            output.append(get_dated_reminder(date, "Vatertag", added_days))
        calendar_list = dbi.select_calendar_by_date(str(date.tm_mday), str(date.tm_mon), str(date.tm_year))
        for elem in calendar_list:
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

def is_mothersday(date):
    return len(dbi.select_mothersdays(str(date.tm_mday), str(date.tm_mon), str(date.tm_year))) == 1

def is_fathersday(date):
    return len(dbi.select_fathersdays(str(date.tm_mday), str(date.tm_mon), str(date.tm_year))) == 1

def get_date(added_days):
    return time.localtime(time.time() + added_days * 86400)