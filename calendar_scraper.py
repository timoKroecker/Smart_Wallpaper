import time
import os
import codecs

from data import calendar_categories as cc
from data import text_file_header as header
from data import weekdays

def scrape_calendar(added_days):
    calendar_dir = manage_dir_structure()

    calendar_list = extract_content_list(calendar_dir + "/" + cc[0][0] + ".txt")
    mothersday_list = extract_content_list(calendar_dir + "/" + cc[1][0] + ".txt")
    fathersday_list = extract_content_list(calendar_dir + "/" + cc[2][0] + ".txt")

    todays_list, num_events_today = get_daily_reminders(added_days, calendar_list, mothersday_list, fathersday_list)
    months_list = get_monthly_reminders(added_days, calendar_list, mothersday_list, fathersday_list)

    return [todays_list, num_events_today, months_list]

def manage_dir_structure():
    calendar_dir = os.path.dirname(os.path.realpath(__file__)) + "/calendar"
    if(not os.path.isdir(calendar_dir)):
        os.mkdir(calendar_dir)
    for file_data in cc:
        file_dir = calendar_dir + "/" + file_data[0] + ".txt"
        if(not os.path.isfile(file_dir)):
            txt_file = codecs.open(file_dir, "w+", "utf-8")
            txt_file.write(header[0] + file_data[0] + file_data[1] + header[1])
    return calendar_dir

def extract_content_list(file_dir):
    content = read_txt_file_contents(file_dir)
    if(content == None):
        return None
    temp_content_list = content.split("\n")
    final_content_list = []
    for string in temp_content_list:
        if(string != ""):
            if(string[-1] == "\r"):
                final_content_list.append(string[0:-1].split("\t"))
            else:
                final_content_list.append(string.split("\t"))
    return final_content_list

def read_txt_file_contents(file_dir):
    if(not os.path.isfile(file_dir)):
        return None
    txt_file = codecs.open(file_dir, "r", "utf-8")
    txt_str = txt_file.read()
    num_caption_lines = 7
    index = 0
    while(num_caption_lines > 0):
        if(txt_str[index] == "\n"):
            num_caption_lines = num_caption_lines - 1
        index = index + 1
    return txt_str[index:len(txt_str)]

def get_daily_reminders(added_days, calendar_list, mothersday_list, fathersday_list):
    date = get_date(added_days)
    output = []
    num_events = 0
    if(is_mothersday(date, mothersday_list)):
        num_events = num_events + 1
        entry = []
        entry.append("Muttertag")
        entry.append("")
        output.append(entry)
    if(is_fathersday(date, fathersday_list)):
        num_events = num_events + 1
        entry = []
        entry.append("Vatertag")
        entry.append("")
        output.append(entry)
    for item in calendar_list:
        if(int(item[0]) == date.tm_mday and int(item[1]) == date.tm_mon):
            num_events = num_events + 1
            entry = []
            entry.append(item[3])
            if(int(item[2]) != 0):
                entry.append(str(date.tm_year - int(item[2])))
            else:
                entry.append("")
            output.append(entry)
    return output, num_events

def get_monthly_reminders(added_days, calendar_list, mothersday_list, fathersday_list):
    output= []
    for i in range(31):
        date = get_date(added_days + i + 1)
        if(is_mothersday(date, mothersday_list)):
            output.append(get_dated_reminder(date, "Muttertag", added_days))
        if(is_fathersday(date, fathersday_list)):
            output.append(get_dated_reminder(date, "Vatertag", added_days))
        for item in calendar_list:
            if(int(item[0]) == date.tm_mday and int(item[1]) == date.tm_mon):
                output.append(get_dated_reminder(date, item[3], added_days))
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

def is_mothersday(date, mothersday_list):
    for item in mothersday_list:
        if(date.tm_mday == int(item[0]) and date.tm_mon == int(item[1]) and date.tm_year == int(item[2])):
            return True
    return False

def is_fathersday(date, fathersday_list):
    for item in fathersday_list:
        if(date.tm_mday == int(item[0]) and date.tm_mon == int(item[1]) and date.tm_year == int(item[2])):
            return True
    return False

def get_date(added_days):
    return time.localtime(time.time() + added_days * 86400)