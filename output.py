import time

def heading():
    print("\n\n--------------------------------------------------")
    print("                  SMART WALLPAPER")
    print("--------------------------------------------------")
    print("")

def calendar_intro(pre = 1, post = 0):
    tab(pre)
    print("~calendar")
    tab(post)

def birthdays_intro(pre = 1, post = 0):
    tab(pre)
    print("~birthdays")
    tab(post)

def expenditure_intro(pre = 1, post = 0):
    tab(pre)
    print("~expenditure")
    tab(post)

def news_intro(pre = 1, post = 0):
    tab(pre)
    print("~news")
    tab(post)

def weather_intro(pre = 1, post = 0):
    tab(pre)
    print("~weather")
    tab(post)

def incidents_intro(pre = 1, post = 0):
    tab(pre)
    print("~incidents")
    tab(post)

def university_intro(pre = 1, post = 0):
    tab(pre)
    print("~university")
    tab(post)

def visible():
    print("\t\tvisible")

def hidden():
    print("\t\thidden")

def final_words():
    print("")
    print("--------------------------------------------------")
    print("                   SHUT DOWN")
    print("--------------------------------------------------")

def terminal_heading():
    print("\n\n--------------------------------------------------")
    print("             SMART WALLPAPER TERMINAL")
    print("--------------------------------------------------")
    print("type 'help' for actions at any step")
    print("")

def home(pre = 1, post = 1):
    tab(pre)
    print("~home")
    tab(post)

def mothersdays_intro(pre = 1, post = 0):
    tab(pre)
    print("~mothersdays")
    tab(post)

def fathersdays_intro(pre = 1, post = 0):
    tab(pre)
    print("~fathersdays")
    tab(post)

def recurring_expenditure_intro(pre = 1, post = 0):
    tab(pre)
    print("~recurring expenditure")
    tab(post)

def keywords_intro(pre = 1, post = 0):
    tab(pre)
    print("~keywords")
    tab(post)

def books_intro(pre = 1, post = 0):
    tab(pre)
    print("~books")
    tab(post)

def library_intro(pre = 1, post = 0):
    tab(pre)
    print("~library")
    tab(post)

def table(table, tabs = 0):
    if(len(table) == 0):
        return
    tab_tracker = []
    for i in range(len(table[0])):
        tab_tracker.append(1)
    for row in table:
        for i in range(len(row)):
            min_tabs = len(str(row[i])) // 8 + 1
            tab_tracker[i] = max(tab_tracker[i], min_tabs)
    for row in table:
        string = ""
        for i in range(len(row)):
            min_tabs = len(str(row[i])) // 8 + 1
            string = string + str(row[i])
            for j in range(tab_tracker[i] - min_tabs + 1):
                string = string + "\t"
        tab_print(tabs, 0, string)

def tab_print(pre, post, string):
    tab(pre)
    print(string)
    tab(post)

def tab(count):
    for i in range(count):
        print("\t", end = '')