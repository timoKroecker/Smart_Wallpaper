import time

import data as da

def get_date(added_days):
    return time.localtime(time.time() + added_days * 86400)

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

def is_mothersday(date):
    for item in da.mothersday:
        if(date.tm_mday == item[0] and date.tm_mon == item[1] and date.tm_year == item[2]):
            return True
    return False

def is_fathersday(date):
    for item in da.fathersday:
        if(date.tm_mday == item[0] and date.tm_mon == item[1] and date.tm_year == item[2]):
            return True
    return False

def get_daily_reminders(added_days):
    date = get_date(added_days)
    output = []
    num_events = 0
    if(is_mothersday(date)):
        num_events = num_events + 1
        entry = []
        entry.append("Muttertag")
        entry.append("")
        output.append(entry)
    if(is_fathersday(date)):
        num_events = num_events + 1
        entry = []
        entry.append("Vatertag")
        entry.append("")
        output.append(entry)
    for item in da.birthdays:
        if(item[0] == date.tm_mday and item[1] == date.tm_mon):
            num_events = num_events + 1
            entry = []
            entry.append(item[3])
            if(item[2] != 0):
                entry.append(str(date.tm_year - item[2]))
            else:
                entry.append("")
            output.append(entry)
    return output, num_events

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

def get_monthly_reminders(added_days):
    output= []
    for i in range(31):
        date = get_date(added_days + i + 1)
        if(is_mothersday(date)):
            output.append(get_dated_reminder(date, "Muttertag", added_days))
        if(is_fathersday(date)):
            output.append(get_dated_reminder(date, "Vatertag", added_days))
        for item in da.birthdays:
            if(item[0] == date.tm_mday and item[1] == date.tm_mon):
                output.append(get_dated_reminder(date, item[3], added_days))
    return output