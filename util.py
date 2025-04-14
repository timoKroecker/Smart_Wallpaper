import time

def get_date(added_days):
    return time.localtime(time.time() + added_days * 86400)