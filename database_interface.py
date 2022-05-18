import sqlite3
import time
import os

from numpy import insert

from data import months as mnths
from data import expence_categories as ec

def create_calendar_tables():
    connection = sqlite3.connect("smart_wallpaper.db")
    cursor = connection.cursor()
    create_calendar(cursor)
    create_mothersdays(cursor)
    create_fathersdays(cursor)
    connection.commit()
    connection.close()

def create_birthday_tables():
    connection = sqlite3.connect("smart_wallpaper.db")
    cursor = connection.cursor()
    create_birthdays(cursor)
    connection.commit()
    connection.close()

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

def create_university_tables():
    connection = sqlite3.connect("smart_wallpaper.db")
    cursor = connection.cursor()
    create_university(cursor)
    connection.commit()
    connection.close()

def create_calendar(cursor):
    try:
        cursor.execute("""
            CREATE TABLE calendar(
                name text,
                day integer,
                month integer,
                year integer
            )
            """)
    except:
        pass

def create_mothersdays(cursor):
    try:
        cursor.execute("""
            CREATE TABLE mothersdays(
                day integer,
                month integer,
                year integer
            )
            """)
    except:
        pass

def create_fathersdays(cursor):
    try:
        cursor.execute("""
            CREATE TABLE fathersdays(
                day integer,
                month integer,
                year integer
            )
            """)
    except:
        pass

def create_birthdays(cursor):
    try:
        cursor.execute("""
            CREATE TABLE birthdays(
                name text,
                day integer,
                month integer,
                year integer
            )
            """)
    except:
        pass

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
                end_month integer,
                end_year integer,
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

def create_university(cursor):
    try:
        cursor.execute("""
            CREATE TABLE university(
                name text,
                day integer,
                month integer,
                year integer
            )
            """)
    except:
        pass

#------------------------------------------------------------------------------------
#Insert into functions

def insert_into_calendar(input_list):
    if(check_calendar(input_list[0], input_list[1], input_list[2], input_list[3])):
        connection = sqlite3.connect("smart_wallpaper.db")
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO calendar
            VALUES('""" + input_list[0] + """', """ + input_list[1] + """, """ + input_list[2] + """, 
            """ + input_list[3] + """)""")
        connection.commit()
        connection.close()
        return True
    return False

def insert_into_mothersdays(input_list):
    if(check_mothersdays(input_list[0], input_list[1], input_list[2])):
        connection = sqlite3.connect("smart_wallpaper.db")
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO mothersdays
            VALUES(""" + input_list[0] + """, """ + input_list[1] + """, 
            """ + input_list[2] + """)""")
        connection.commit()
        connection.close()
        return True
    return False

def insert_into_fathersdays(input_list):
    if(check_fathersdays(input_list[0], input_list[1], input_list[2])):
        connection = sqlite3.connect("smart_wallpaper.db")
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO fathersdays
            VALUES(""" + input_list[0] + """, """ + input_list[1] + """, 
            """ + input_list[2] + """)""")
        connection.commit()
        connection.close()
        return True
    return False

def insert_into_birthdays(input_list):
    if(check_birthdays(input_list[0])):
        connection = sqlite3.connect("smart_wallpaper.db")
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO birthdays
            VALUES('""" + input_list[0] + """', """ + input_list[1] + """, """ + input_list[2] + """, 
            """ + input_list[3] + """)""")
        connection.commit()
        connection.close()
        return True
    return False

def insert_into_expenditure(input_list):
    connection = sqlite3.connect("smart_wallpaper.db")
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO expenditure
        VALUES('""" + input_list[0] + """', """ + input_list[1] + """, """ + input_list[2] + """, 
        """ + input_list[3] + """, '""" + input_list[4] + "', """ + input_list[5] + """)
        """)
    connection.commit()
    connection.close()
    return True

def insert_into_recurring_expenditure(input_list):
    connection = sqlite3.connect("smart_wallpaper.db")
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO recurring_expenditure
        VALUES('""" + input_list[0] + """', '""" + input_list[1] + "', """ + input_list[2] + """, 
        """ + input_list[3] + """, """ + input_list[4] + """, """ + input_list[5] + """, """ + input_list[6] + """)
        """)
    connection.commit()
    connection.close()
    return True

def insert_into_expenditures_from_recurring_expenditure(added_days):
    rec_exp_matrix = select_recurring_expenditure()
    for row in rec_exp_matrix:
        name = row[0]
        category = row[1]
        start_month = row[2]
        start_year = row[3]
        end_month = row[4]
        end_year = row[5]
        amount = row[6]
        if(check_recurring_expenditure(added_days, name, category, start_month, start_year, end_month, end_year, amount)):
            date = get_localtime(added_days)
            insert_into_expenditure([name, "1", str(date.tm_mon), str(date.tm_year), category, str(amount)])

def insert_into_incidents(input_list):
    if(check_incidents(input_list[0], input_list[1], input_list[2], input_list[3])):
        connection = sqlite3.connect("smart_wallpaper.db")
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO incidents
            VALUES ('""" + input_list[0] + """', """ + input_list[1] + """, """ + input_list[2] + """, 
            """ + input_list[3] + """, """ + input_list[4] + """)
            """)
        connection.commit()
        connection.close()
        return True
    return False

def insert_into_keywords(input_list):
    if(check_keywords(input_list[0])):
        connection = sqlite3.connect("smart_wallpaper.db")
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO keywords
            VALUES ('""" + input_list[0] + """', """ + input_list[1] + """)
            """)
        connection.commit()
        connection.close()
        return True
    return False

def insert_into_university(input_list):
    if(check_university(input_list[0], input_list[1], input_list[2], input_list[3])):
        connection = sqlite3.connect("smart_wallpaper.db")
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO university
            VALUES('""" + input_list[0] + """', """ + input_list[1] + """, """ + input_list[2] + """, 
            """ + input_list[3] + """)""")
        connection.commit()
        connection.close()
        return True
    return False

#------------------------------------------------------------------------------------
#Select functions

def select_calendar(name, day_str, month_str, year_str):
    connection = sqlite3.connect("smart_wallpaper.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT *
        FROM calendar
        WHERE name = '""" + name + """'
        AND year = """ + year_str + """
        AND month = """ + month_str + """
        AND day = """ + day_str + """
        """)
    fetch = cursor.fetchall()
    connection.commit()
    connection.close()
    return fetch

def select_calendar_by_date(day_str, month_str, year_str):
    connection = sqlite3.connect("smart_wallpaper.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT *
        FROM calendar
        WHERE day = """ + day_str + """
        AND month = """ + month_str + """
        AND (year = """ + year_str + """
        OR year = 0)
        """)
    fetch = cursor.fetchall()
    connection.commit()
    connection.close()
    return fetch

def select_mothersdays(day_str, month_str, year_str):
    connection = sqlite3.connect("smart_wallpaper.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT *
        FROM mothersdays
        WHERE year = """ + year_str + """
        AND month = """ + month_str + """
        AND day = """ + day_str + """
        """)
    fetch = cursor.fetchall()
    connection.commit()
    connection.close()
    return fetch

def select_fathersdays(day_str, month_str, year_str):
    connection = sqlite3.connect("smart_wallpaper.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT *
        FROM fathersdays
        WHERE year = """ + year_str + """
        AND month = """ + month_str + """
        AND day = """ + day_str + """
        """)
    fetch = cursor.fetchall()
    connection.commit()
    connection.close()
    return fetch

def select_birthdays(name):
    connection = sqlite3.connect("smart_wallpaper.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT *
        FROM birthdays
        WHERE name = '""" + name + """'
        """)
    fetch = cursor.fetchall()
    connection.commit()
    connection.close()
    return fetch

def select_birthdays_by_date(day_str, month_str):
    connection = sqlite3.connect("smart_wallpaper.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT *
        FROM birthdays
        WHERE day = """ + day_str + """
        AND month = """ + month_str + """
        """)
    fetch = cursor.fetchall()
    connection.commit()
    connection.close()
    return fetch

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

def select_incidents_by_date(date):
    connection = sqlite3.connect("smart_wallpaper.db")
    cursor = connection.cursor()
    day_str = str(date.tm_mday)
    month_str = str(date.tm_mon)
    year_str = str(date.tm_year)
    cursor.execute("""
        SELECT name, value
        FROM incidents
        WHERE day = """ + day_str + """
        AND month = """ + month_str + """
        AND year = """ + year_str + """
        """)
    fetch = cursor.fetchall()
    connection.commit()
    connection.close()
    return fetch

def select_incidents_plot_cube(range_of_days):
    cube = []
    connection = sqlite3.connect("smart_wallpaper.db")
    cursor = connection.cursor()
    for i in range(range_of_days):
        added_days = -(range_of_days - 1) + i
        date = get_localtime(added_days)
        day_str = str(date.tm_mday)
        month_str = str(date.tm_mon)
        year_str = str(date.tm_year)
        cursor.execute("""
            SELECT *
            FROM incidents
            WHERE day = """ + day_str + """
            AND month = """ + month_str + """
            AND year = """ + year_str + """
        """)
        fetch = cursor.fetchall()
        cube.append(fetch)
    connection.commit()
    connection.close()
    return cube

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

def select_university(name, day_str, month_str, year_str):
    connection = sqlite3.connect("smart_wallpaper.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT *
        FROM university
        WHERE name = '""" + name + """'
        AND year = """ + year_str + """
        AND month = """ + month_str + """
        AND day = """ + day_str + """
        """)
    fetch = cursor.fetchall()
    connection.commit()
    connection.close()
    return fetch

def select_university_by_date(day_str, month_str, year_str):
    connection = sqlite3.connect("smart_wallpaper.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT *
        FROM university
        WHERE day = """ + day_str + """
        AND month = """ + month_str + """
        AND (year = """ + year_str + """
        OR year = 0)
        """)
    fetch = cursor.fetchall()
    connection.commit()
    connection.close()
    return fetch

def select_table(table):
    connection = sqlite3.connect("smart_wallpaper.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT rowid, *
        FROM """ + table + """
        """)
    fetch = cursor.fetchall()
    connection.commit()
    connection.close()
    return fetch

def select_by_rowid(rowid, tablename):
    connection = sqlite3.connect("smart_wallpaper.db")
    cursor = connection.cursor()
    cursor.execute("""
        SELECT rowid, *
        FROM """ + tablename + """
        WHERE rowid = """ + rowid + """
        """)
    fetch = cursor.fetchall()
    connection.commit()
    connection.close()
    return fetch

#------------------------------------------------------------------------------------
#Check functions

def check_calendar(name, day_str, month_str, year_str):
    return len(select_calendar(name, day_str, month_str, year_str)) == 0

def check_mothersdays(day_str, month_str, year_str):
    return len(select_mothersdays(day_str, month_str, year_str)) == 0

def check_fathersdays(day_str, month_str, year_str):
    return len(select_fathersdays(day_str, month_str, year_str)) == 0

def check_birthdays(name):
    return len(select_birthdays(name)) == 0

def check_recurring_expenditure(added_days, name, category, start_month, start_year, end_month, end_year, amount):
    month = get_localtime(added_days).tm_mon
    year = get_localtime(added_days).tm_year
    if( (not check_rexp_zeros(start_month, start_year) and
            check_rexp_start_out_of_bounds(added_days, start_month, start_year))
        or
        (not check_rexp_zeros(end_month, end_year) and
            check_rexp_end_out_of_bounds(added_days, end_month, end_year))
        ):
        return False
    if(len(select_expenditure(name, category, str(month), str(year), str(amount))) != 0):
        return False
    return True

def check_rexp_zeros(month, year):
    return month == 0 and year == 0

def check_rexp_start_out_of_bounds(added_days, start_month, start_year):
    month = get_localtime(added_days).tm_mon
    year = get_localtime(added_days).tm_year
    if(year < start_year or (year == start_year and month < start_month)):
        return True
    return False

def check_rexp_end_out_of_bounds(added_days, end_month, end_year):
    month = get_localtime(added_days).tm_mon
    year = get_localtime(added_days).tm_year
    if(year > end_year or (year == end_year and month > end_month)):
        return True
    return False

def check_two_decimals(string):
    if(string[-2] == "."):
        return string + "0"
    return string

def check_incidents(name, day_str, month_str, year_str):
    return len(select_incidents(name, day_str, month_str, year_str)) == 0

def check_keywords(word):
    return len(select_keywords(word)) == 0

def check_university(name, day_str, month_str, year_str):
    return len(select_university(name, day_str, month_str, year_str)) == 0

#------------------------------------------------------------------------------------
#Get functions

def get_localtime(added_days):
    return time.localtime(time.time() + added_days * 86400)

#------------------------------------------------------------------------------------
#Update functions

def update_incidents(name, day_str, month_str, year_str, value_str):
    connection = sqlite3.connect("smart_wallpaper.db")
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE incidents
        SET value = """ + value_str + """
        WHERE name = '""" + name + """'
        AND day = """ + day_str + """
        AND month = """ + month_str + """
        AND year = """ + year_str + """
        """)
    connection.commit()
    connection.close()

#------------------------------------------------------------------------------------
#Delete functions functions

def delete_by_rowid(rowid, tablename):
    connection = sqlite3.connect("smart_wallpaper.db")
    cursor = connection.cursor()
    cursor.execute("""
        DELETE
        FROM """ + tablename + """
        WHERE rowid = """ + rowid + """
        """)
    fetch = cursor.fetchall()
    connection.commit()
    connection.close()
    return fetch

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
    num_caption_lines = 7
    index = 0
    while(num_caption_lines > 0):
        if(txt_str[index] == "\n"):
            num_caption_lines = num_caption_lines - 1
        index = index + 1
    return txt_str[index:len(txt_str)]

#------------------------------------------------------------------------------------
#Test functions

def test_function():
    connection = sqlite3.connect("smart_wallpaper.db")
    cursor = connection.cursor()
    cursor.execute("""
        
        """)
    fetch = cursor.fetchall()
    connection.commit()
    connection.close()
    for row in fetch:
        print(row)

#test_function()