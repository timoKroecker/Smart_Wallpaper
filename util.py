import time

def get_date(added_days):
    return time.localtime(time.time() + added_days * 86400)

def sign(value):
    if value == 0:
        return 0
    if value > 0:
        return 1
    return -1

def format_dm(day, month):
    day = str(day)
    month = str(month)
    if len(day) == 1:
        day = "0" + day
    if len(month) == 1:
        month = "0" + month
    return day + "." + month + "."

def string_to_tex(string: str):
    string = string.replace("&", "\\&")
    return string