import time

import database_interface as dbi

from data import months as mnths
from data import expence_categories as ec

def scrape_finances(added_days):
    dbi.create_finance_tables()
    dbi.insert_into_expenditures_from_recurring_expenditure(added_days)
    return get_months_finances(added_days), get_years_finances(added_days)

def get_months_finances(added_days):
    month_int = get_localtime(added_days).tm_mon
    month_str = str(month_int)
    year_str = str(get_localtime(added_days).tm_year)
    income = dbi.select_monthly_total_income(month_str, year_str)
    expences = dbi.select_monthly_total_expenditure(month_str, year_str)
    saldo = format_amount(str(round(float(income) - float(expences), 2)))
    return [[income, expences, saldo], mnths[month_int - 1][1]]

def get_years_finances(added_days):
    year_str = str(get_localtime(added_days).tm_year)
    income = dbi.select_yearly_total_income(year_str)
    expences = dbi.select_yearly_total_expenditure(year_str)
    saldo = format_amount(str(round(float(income) - float(expences), 2)))
    return [[income, expences, saldo], year_str]

def get_percentage(category_amount, total_amount):
    if(total_amount == 0):
        return "0"
    return str(int(round(100 * float(category_amount) / float(total_amount), 0)))

def format_amount(string):
    if string[-2] == ".":
        return string + "0"
    return string

def get_localtime(added_days):
    return time.localtime(time.time() + added_days * 86400)