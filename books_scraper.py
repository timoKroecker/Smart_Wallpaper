import database_interface as dbi
import time

def scrape_books(added_days, yearly_goal):
    dbi.create_books_tables()
    date = get_date(added_days)
    current_month = date.tm_mon
    current_year = date.tm_year

    monthly_goal = yearly_goal // 12
    cummulative_goal = monthly_goal * current_month
    goals = [monthly_goal, cummulative_goal, yearly_goal]

    books_list = []
    for i in range(current_month):
        month = i + 1 
        monthly_pages = dbi.select_bookpages_by_month_year(str(month), str(current_year))
        if(monthly_pages == None):
            books_list.append(0)
        else:
            books_list.append(monthly_pages)

    prognosis = get_prognosis(sum(books_list), yearly_goal, added_days)

    return max(cummulative_goal, sum(books_list)), goals, books_list, prognosis

def get_prognosis(num_pages, yearly_goal, added_days):
    current_year_day = get_date(added_days).tm_yday
    total_year_days = get_total_year_days(added_days)

    return int(round(num_pages / current_year_day * total_year_days, 0))

def get_total_year_days(added_days):
    day_iterator = 0
    prev_year_day = get_date(added_days).tm_yday
    current_year_day = get_date(added_days).tm_yday

    while(abs(prev_year_day - current_year_day) <= 1):
        prev_year_day = current_year_day
        current_year_day = get_date(added_days + day_iterator).tm_yday
        day_iterator += 1
    
    return prev_year_day

def get_date(added_days):
    return time.localtime(time.time() + added_days * 86400)
