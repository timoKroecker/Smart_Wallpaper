import sqlite3
#from sqlite3.dbapi2 import connect
import time
import os

from data import months as mnths
from data import expence_categories as ec
from data import positive_keywords_1 as pk1
from data import positive_keywords_2 as pk2
from data import negative_keywords_1 as nk1
from data import negative_keywords_2 as nk2

def create_finance_tables():
    connection = sqlite3.connect("smart_wallpaper.db")
    cursor = connection.cursor()
    create_expenditure(cursor)
    create_recurring_expenditure(cursor)
    connection.commit()
    connection.close()

def create_incidents_tables():
    connection = sqlite3.connect("smart_wallpaper.db")
    cursor = connection.cursor()
    create_incidents(cursor)
    connection.commit()
    connection.close()

def create_news_tables():
    connection = sqlite3.connect("smart_wallpaper.db")
    cursor = connection.cursor()
    create_keywords(cursor)
    connection.commit()
    connection.close()

def create_expenditure(cursor):
    try:
        cursor.execute("""
            CREATE TABLE expenditure(
                name text,
                day integer,
                month integer,
                year integer,
                category text,
                amount real
            )
            """)
    except:
        pass

def create_recurring_expenditure(cursor):
    try:
        cursor.execute("""
            CREATE TABLE recurring_expenditure(
                name text,
                category text,
                start_month intgeger,
                start_year integer,
                amount real
            )
            """)
    except:
        pass

def create_incidents(cursor):
    try:
        cursor.execute("""
            CREATE TABLE incidents(
                name text,
                day integer,
                month intgeger,
                year integer,
                value real
            )
            """)
    except:
        pass

def create_keywords(cursor):
    try:
        cursor.execute("""
            CREATE TABLE keywords(
                word text,
                score real
            )
            """)
    except:
        pass

#------------------------------------------------------------------------------------
#Insert into functions

def insert_into_expenditure(name, day_str, month_str, year_str, category, amount_str):
    connection = sqlite3.connect("smart_wallpaper.db")
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO expenditure
        VALUES('""" + name + """', """ + day_str + """, """ + month_str + """, 
        """ + year_str + """, '""" + category + "', """ + amount_str + """)
        """)
    connection.commit()
    connection.close()

def insert_into_recuuring_expenditure(name, category, start_month, start_year, amount_str):
    connection = sqlite3.connect("smart_wallpaper.db")
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO recurring_expenditure
        VALUES('""" + name + """', '""" + category + "', """ + start_month + """, 
        """ + start_year + """, """ + amount_str + """)
        """)
    connection.commit()
    connection.close()

def insert_into_expenditures_from_recurring_expenditure(added_days):
    rec_exp_matrix = select_recurring_expenditure()
    for row in rec_exp_matrix:
        name = row[0]
        category = row[1]
        start_month = row[2]
        start_year = row[3]
        amount = row[4]
        if(check_recurring_expenditure(added_days, name, category, start_month, start_year, amount)):
            date = get_localtime(added_days)
            insert_into_expenditure(name, "1", str(date.tm_mon), str(date.tm_year), category, str(amount))

def insert_into_incidents(name, day_str, month_str, year_str, value_str):
    if(check_incidents(name, day_str, month_str, year_str)):
        connection = sqlite3.connect("smart_wallpaper.db")
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO incidents
            VALUES ('""" + name + """', """ + day_str + """, """ + month_str + """, 
            """ + year_str + """, """ + value_str + """)
            """)
        connection.commit()
        connection.close()

def insert_into_keywords(word, score_str):
    if(check_keywords(word)):
        connection = sqlite3.connect("smart_wallpaper.db")
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO keywords
            VALUES ('""" + word + """', """ + score_str + """)
            """)
        connection.commit()
        connection.close()

#------------------------------------------------------------------------------------
#Select functions

def select_expenditure(name, category, month_str, year_str, amount):
    connection = sqlite3.connect("smart_wallpaper.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT *
        FROM expenditure
        WHERE name = '""" + name + """'
        AND year = """ + year_str + """
        AND month = """ + month_str + """
        AND category = '""" + category + """'
        AND amount = """ + amount + """
        """)
    fetch = cursor.fetchall()
    connection.commit()
    connection.close()
    return fetch

def select_recurring_expenditure():
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

def select_monthly_total_expenditure(month_str, year_str):
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

def select_monthly_category_expenditure(month_str, year_str, category):
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

def select_yearly_total_expenditure(year_str):
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

def select_yearly_category_expenditure(year_str, category):
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

def select_incidents(name, day_str, month_str, year_str):
    connection = sqlite3.connect("smart_wallpaper.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT *
        FROM incidents
        WHERE name = '""" + name + """'
        AND day = """ + day_str + """
        AND month = """ + month_str + """
        AND year = """ + year_str + """
        """)
    fetch = cursor.fetchall()
    connection.commit()
    connection.close()
    return fetch

def select_keywords(word):
    connection = sqlite3.connect("smart_wallpaper.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT  *
        FROM keywords
        WHERE word = '""" + word + """'
        """)
    fetch = cursor.fetchall()
    connection.commit()
    connection.close()
    return fetch

def select_score(word):
    connection = sqlite3.connect("smart_wallpaper.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT  score
        FROM keywords
        WHERE word = '""" + word + """'
        """)
    fetch = cursor.fetchall()
    connection.commit()
    connection.close()
    if(len(fetch) == 0): return "0.0"
    return fetch[0][0]

#------------------------------------------------------------------------------------
#Check functions

def check_recurring_expenditure(added_days, name, category, start_month, start_year, amount):
    month = get_localtime(added_days).tm_mon
    year = get_localtime(added_days).tm_year
    if(year < start_year or (year == start_year and month < start_month)):
        return False
    if(len(select_expenditure(name, category, str(month), str(year), str(amount))) != 0):
        return False
    return True

def check_two_decimals(string):
    if(string[-2] == "."):
        return string + "0"
    return string

def check_incidents(name, day_str, month_str, year_str):
    return len(select_incidents(name, day_str, month_str, year_str)) == 0

def check_keywords(word):
    return len(select_keywords(word)) == 0

#------------------------------------------------------------------------------------
#Get functions

def get_localtime(added_days):
    return time.localtime(time.time() + added_days * 86400)

#------------------------------------------------------------------------------------
#In case of dropping finance tables

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

#------------------------------------------------------------------------------------
#In case of dropping keywords table

#------------------------------------------------------------------------------------
#Test functions

def test_query():
    connection = sqlite3.connect("smart_wallpaper.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT rowid, *
        FROM incidents
        """)
    fetch = cursor.fetchall()
    connection.commit()
    connection.close()
    for row in fetch:
        print(row)