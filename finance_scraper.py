import time

import database_interface as dbi

from data import months as mnths
from data import expence_categories as ec

def scrape_finances(added_days):
    dbi.create_finance_tables()
    dbi.insert_into_expenditures_from_recurring_expenditure(added_days)
    return [get_months_expences(added_days), get_years_expences(added_days)]

def get_months_expences(added_days):
    month_int = get_localtime(added_days).tm_mon
    month_str = str(month_int)
    year_str = str(get_localtime(added_days).tm_year)
    expences = []
    total = ["Gesamt:"]

    fetch = dbi.select_monthly_total_expenditure(month_str, year_str)
    total.append(fetch)
    for i in range(len(ec)):
        category = ec[i][1]
        category_array = [category + ":"]
        fetch = dbi.select_monthly_category_expenditure(month_str, year_str, category)
        category_array.append(fetch)
        category_array.append(get_percentage(category_array[1], total[1]))
        expences.append(category_array)
    return [expences, total, mnths[month_int - 1][1]]

def get_years_expences(added_days):
    year_str = str(get_localtime(added_days).tm_year)
    expences = []
    total = ["Gesamt:"]

    fetch = dbi.select_yearly_total_expenditure(year_str)
    total.append(fetch)
    for i in range(len(ec)):
        category = ec[i][1]
        category_array = [category + ":"]
        fetch = dbi.select_yearly_category_expenditure(year_str, category)
        category_array.append(fetch)
        category_array.append(get_percentage(category_array[1], total[1]))
        expences.append(category_array)
    return [expences, total, year_str]

def get_percentage(category_amount, total_amount):
    if(total_amount == 0):
        return "0"
    return str(int(round(100 * float(category_amount) / float(total_amount), 0)))

def get_localtime(added_days):
    return time.localtime(time.time() + added_days * 86400)