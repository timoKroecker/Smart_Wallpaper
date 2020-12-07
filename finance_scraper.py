import time
import os
import re

from data import months as mnths
from data import expence_categories as ec

def scrape_finances(added_days):
    finance_dir, month_dir = manage_dir_structure(added_days)
    manage_file_structure(finance_dir, month_dir)
    return [get_months_expences(added_days), get_years_expences(added_days)]

def manage_dir_structure(added_days):
    finance_dir = os.path.dirname(os.path.realpath(__file__)) + "\\finances"
    year_dir = finance_dir + "\\" + str(get_localtime(added_days).tm_year)
    month_dir = year_dir + "\\" + mnths[get_localtime(added_days).tm_mon - 1][0]
    if(not os.path.isdir(finance_dir)):
        os.mkdir(finance_dir)
    if(not os.path.isdir(year_dir)):
        os.mkdir(year_dir)
    if(not os.path.isdir(month_dir)):
        os.mkdir(month_dir)
    return finance_dir, month_dir

def manage_file_structure(finance_dir, month_dir):
    txt_files = []
    header_1 = "+++++++++++++++++++++\n"
    header_2 = "\n+++++++++++++++++++++\n\n|||||||||||||||||||||\nvvvvvvvvvvvvvvvvvvvvv\n"
    global_contents_list = manage_global_files(finance_dir, header_1, header_2)
    for i in range(len(ec)):
        file_name = ec[i][0]
        header_merge = header_1 + file_name + header_2
        if(not os.path.isfile(month_dir + "\\" + file_name + ".txt")):
            new_file = open(month_dir + "\\" + file_name + ".txt", "w+")
            new_file.write(header_merge + global_contents_list[i])
            txt_files.append(new_file)
        else:
            txt_files.append(open(month_dir + "\\" + file_name + ".txt", "r"))
    return txt_files

def manage_global_files(finance_dir, header_1, header_2):
    contents_list = []
    for category in ec:
        header_merge = header_1 + category[0] + header_2
        file_name = category[0] + "_global"
        contents = ""
        if(not os.path.isfile(finance_dir + "\\" + file_name + ".txt")):
            glob_file = open(finance_dir + "\\" + file_name + ".txt", "w+")
            glob_file.write(header_merge)
        else:
            contents = read_txt_file_contents(finance_dir + "\\" + file_name + ".txt")
            contents_list.append(contents)
    return contents_list

def get_months_expences(added_days):
    month_int = get_localtime(added_days).tm_mon - 1
    month_str = mnths[month_int][0]
    year_str = str(get_localtime(added_days).tm_year)
    month_dir = os.path.dirname(os.path.realpath(__file__)) + "\\finances\\" + year_str + "\\" + month_str

    expences = []
    total = ["Gesamt:"]
    for i in range(len(ec)):
        file_name = ec[i][0] + ".txt"
        content_list = extract_content_list(month_dir + "\\" + file_name)
        entry = []
        entry.append(ec[i][1] + ":")
        entry.append(get_content_list_sum(content_list))
        expences.append(entry)
    total.append(get_content_list_sum(expences))
    for entry in expences:
        entry.append(str(int(round(float(entry[1]) / float(total[1]) * 100, 0))))
    return [expences, total, mnths[month_int][1]]

def get_years_expences(added_days):
    year_str = str(get_localtime(added_days).tm_year)
    year_dir = os.path.dirname(os.path.realpath(__file__)) + "\\finances\\" + year_str

    expences = []
    total = ["Gesamt:"]
    for i in range(len(ec)):
        file_name = ec[i][0] + ".txt"
        category_sum = 0.0
        month_content_list = []
        for j in range(12):
            month_dir = year_dir + "\\" + mnths[j][0]
            if(os.path.isdir(month_dir)):
                content_list = extract_content_list(month_dir + "\\" + file_name)
                entry = []
                entry.append(mnths[j][0])
                entry.append(get_content_list_sum(content_list))
                month_content_list.append(entry)
        entry = []
        entry.append(ec[i][1] + ":")
        entry.append(get_content_list_sum(month_content_list))
        expences.append(entry)
    total.append(get_content_list_sum(expences))
    for entry in expences:
        entry.append(str(int(round(float(entry[1]) / float(total[1]) * 100, 0))))
    return [expences, total, year_str]

def extract_content_list(file_dir):
    content_str = read_txt_file_contents(file_dir)
    temp_content_list = content_str.split("\n")
    final_content_list = []
    for string in temp_content_list:
        if(string != ""):
            final_content_list.append(string.split("\t"))
    return final_content_list

def read_txt_file_contents(file_dir):
    if(not os.path.isfile(file_dir)):
        return None
    txt_file = open(file_dir, "r")
    txt_str = txt_file.read()
    num_caption_lines = 6
    index = 0
    while(num_caption_lines > 0):
        if(txt_str[index] == "\n"):
            num_caption_lines = num_caption_lines - 1
        index = index + 1
    return txt_str[index:len(txt_str)]

def get_content_list_sum(content_list):
    content_sum = 0.0
    for entry in content_list:
        content_sum = round(content_sum + float(entry[1]), 2)
    string = str(content_sum)
    if(string[-2] == "."):
        string = string + "0"
    return string

def get_localtime(added_days):
    return time.localtime(time.time() + added_days * 86400)