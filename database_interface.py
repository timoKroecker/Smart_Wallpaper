import sqlite3
import time
import os

from data import months as mnths
from data import expence_categories as ec

def create_tables():
    connection = sqlite3.connect("smart_wallpaper.db")
    cursor = connection.cursor()
    try:
        cursor.execute("""
            CREATE TABLE expenditure(
                title text,
                day integer,
                month integer,
                year integer,
                category text,
                amount real
            )
            """)
    except:
        pass
    try:
        cursor.execute("""
            CREATE TABLE recurring_expenditure(
                title text,
                category text,
                start_month intgeger,
                start_year integer,
                amount real
            )
            """)
    except:
        pass
    connection.commit()
    connection.close()

def add_expenditures_from_recurring_expenditure(added_days):
    rec_exp_matrix = select_all_recurring_expenditure()
    for row in rec_exp_matrix:
        title = row[0]
        category = row[1]
        start_month = row[2]
        start_year = row[3]
        amount = row[4]
        if(check_recurring_expenditure(title, category, start_month, start_year, amount)):
            date = get_localtime(added_days)
            insert_into_expenditure(title, date.tm_mday, date.tm_mon, date.tm_year, category, amount)

def check_recurring_expenditure(title, category, start_month, start_year, amount):
    pass

def insert_into_expenditure(title, day, month, year, category, amount):
    pass

def select_all_recurring_expenditure():
    connection = sqlite3.connect("smart_wallpaper.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT *
        FROM recurring_expenditure
        """)
    fetch = cursor.fetchall()
    connection.commit()
    connection.close()
    return fetch

def read_finance_directory(year_str):
    connection = sqlite3.connect("smart_wallpaper.db")
    cursor = connection.cursor()
    year_dir = manage_dir_structure(year_str)
    for i in range(12):
        month_dir = year_dir + "/" + mnths[i][0]
        if(os.path.isdir(month_dir)):
            for ec_row in ec:
                category_dir = month_dir + "/" + ec_row[0] + ".txt"
                content_matrix = extract_content_list(category_dir)
                for content_row in content_matrix:
                    cursor.execute("""
                        INSERT INTO expenditure
                        VALUES ('""" + content_row[0] + """', 1, """ + str(i + 1) + """, """ + year_str + """, '""" + ec_row[1] + """', """ + content_row[1] + """)
                        """)
    connection.commit()
    connection.close()

def manage_dir_structure(year_str):
    finance_dir = os.path.dirname(os.path.realpath(__file__)) + "/finances"
    year_dir = finance_dir + "/" + year_str
    return year_dir

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

def get_monthly_total_expenditure(month_str, year_str):
    connection = sqlite3.connect("smart_wallpaper.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT sum(amount)
        FROM expenditure
        WHERE year = """ + year_str + """
        AND month = """ + month_str + """
        """)
    fetch = cursor.fetchall()[0][0]
    connection.commit()
    connection.close()
    if(fetch == None):
        return "0.00"
    return check_two_decimals(str(round(fetch, 2)))

def get_monthly_category_expenditure(month_str, year_str, category):
    connection = sqlite3.connect("smart_wallpaper.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT sum(amount)
        FROM expenditure
        WHERE year = """ + year_str + """
        AND month = """ + month_str + """
        AND category = '""" + category + """'
        """)
    fetch = cursor.fetchall()[0][0]
    connection.commit()
    connection.close()
    if(fetch == None):
        return "0.00"
    return check_two_decimals(str(round(fetch, 2)))

def get_yearly_total_expenditure(year_str):
    connection = sqlite3.connect("smart_wallpaper.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT sum(amount)
        FROM expenditure
        WHERE year = """ + year_str + """
        """)
    fetch = cursor.fetchall()[0][0]
    connection.commit()
    connection.close()
    if(fetch == None):
        return "0.00"
    return check_two_decimals(str(round(fetch, 2)))

def get_yearly_category_expenditure(year_str, category):
    connection = sqlite3.connect("smart_wallpaper.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT sum(amount)
        FROM expenditure
        WHERE year = """ + year_str + """
        AND category = '""" + category + """'
        """)
    fetch = cursor.fetchall()[0][0]
    connection.commit()
    connection.close()
    if(fetch == None):
        return "0.00"
    return check_two_decimals(str(round(fetch, 2)))

def check_two_decimals(string):
    if(string[-2] == "."):
        return string + "0"
    return string

def insert_into_recuuring_expenditure(title, category, start_month, start_year, amount):
    connection = sqlite3.connect("smart_wallpaper.db")
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO recurring_expenditure
        VALUES('""" + title + """', '""" + category + "', """ + start_month + """, """ + start_year + """, """ + amount + """)
        """)
    connection.commit()
    connection.close()

def test_query():
    connection = sqlite3.connect("smart_wallpaper.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT *
        FROM recurring_expenditure
        """)
    fetch = cursor.fetchall()
    for elem in fetch:
        print(elem)
    connection.commit()
    connection.close()

def get_localtime(added_days):
    return time.localtime(time.time() + added_days * 86400)