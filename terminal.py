import output as op
import database_interface as dbi

ZERO = 0
DIRECTORY = 1
INPUT = 2
OUTPUT = 3

def the_one_ring():
    op.terminal_heading()
    op.home(post = INPUT)
    terminal_input = input()
    while(terminal_input != "stop"):
        if(terminal_input == "cal"):
            calendar_terminal()
        elif(terminal_input == "bir"):
            birthday_terminal()
        elif(terminal_input == "exp"):
            expenditure_terminal()
        elif(terminal_input == "news"):
            news_terminal()
        elif(terminal_input == "inc"):
            incidents_terminal()
        elif(terminal_input == "uni"):
            university_terminal()
        elif(terminal_input == "help"):
            op.tab_print(OUTPUT, 0, "cal, bir, exp, news, inc, uni, stop")
        else:
            op.tab_print(OUTPUT, 0, "command not found")
        op.home(post = 2)
        terminal_input = input()

    op.final_words()

#-------------------------------------------------------------------
#Terminals

def calendar_terminal():
    op.home(post = ZERO)
    op.calendar_intro(post = INPUT)
    terminal_input = input()
    while(terminal_input != "back"):
        if(terminal_input == "show"):
            table = dbi.select_table("calendar")
            op.table(table, tabs = OUTPUT)
        elif(terminal_input == "insert"):
            insert("calendar")
        elif(terminal_input == "delete"):
            delete("calendar")
        elif(terminal_input == "moth"):
            mothersdays_terminal()
        elif(terminal_input == "fath"):
            fathersdays_terminal()
        elif(terminal_input == "update"):
            update("calendar")
        elif(terminal_input == "help"):
            op.tab_print(OUTPUT, 0, "show, insert, delete, moth, fath, back")
        else:
            op.tab_print(OUTPUT, 0, "command not found")

        op.home(post = ZERO)
        op.calendar_intro(post = INPUT)
        terminal_input = input()

def mothersdays_terminal():
    op.home(post = ZERO)
    op.calendar_intro()
    op.mothersdays_intro(post = INPUT)
    terminal_input = input()
    while(terminal_input != "back"):
        if(terminal_input == "show"):
            table = dbi.select_table("mothersdays")
            op.table(table, tabs = OUTPUT)
        elif(terminal_input == "insert"):
            insert("mothersdays")
        elif(terminal_input == "delete"):
            delete("mothersdays")
        elif(terminal_input == "update"):
            update("mothersdays")
        elif(terminal_input == "help"):
            op.tab_print(OUTPUT, 0, "show, insert, delete, back")
        else:
            op.tab_print(OUTPUT, 0, "command not found")

        op.home(post = ZERO)
        op.calendar_intro()
        op.mothersdays_intro(post = INPUT)
        terminal_input = input()

def fathersdays_terminal():
    op.home(post = ZERO)
    op.calendar_intro()
    op.fathersdays_intro(post = INPUT)
    terminal_input = input()
    while(terminal_input != "back"):
        if(terminal_input == "show"):
            table = dbi.select_table("fathersdays")
            op.table(table, tabs = OUTPUT)
        elif(terminal_input == "insert"):
            insert("fathersdays")
        elif(terminal_input == "delete"):
            delete("fathersdays")
        elif(terminal_input == "update"):
            update("fathersdays")
        elif(terminal_input == "help"):
            op.tab_print(OUTPUT, 0, "show, insert, delete, back")
        else:
            op.tab_print(OUTPUT, 0, "command not found")

        op.home(post = ZERO)
        op.calendar_intro()
        op.fathersdays_intro(post = INPUT)
        terminal_input = input()

def birthday_terminal():
    op.home(post = ZERO)
    op.birthdays_intro(post = INPUT)
    terminal_input = input()
    while(terminal_input != "back"):
        if(terminal_input == "show"):
            table = dbi.select_table("birthdays")
            op.table(table, tabs = OUTPUT)
        elif(terminal_input == "insert"):
            insert("birthdays")
        elif(terminal_input == "delete"):
            delete("birthdays")
        elif(terminal_input == "update"):
            update("birthdays")
        elif(terminal_input == "help"):
            op.tab_print(OUTPUT, 0, "show, insert, delete, back")
        else:
            op.tab_print(OUTPUT, 0, "command not found")

        op.home(post = ZERO)
        op.birthdays_intro(post = INPUT)
        terminal_input = input()

def expenditure_terminal():
    op.home(post = ZERO)
    op.expenditure_intro(post = INPUT)
    terminal_input = input()
    while(terminal_input != "back"):
        if(terminal_input == "show"):
            table = dbi.select_table("expenditure")
            op.table(table, tabs = OUTPUT)
        elif(terminal_input == "insert"):
            insert("expenditure")
        elif(terminal_input == "delete"):
            delete("expenditure")
        elif(terminal_input == "rexp"):
            recurring_expenditure_terminal()
        elif(terminal_input == "update"):
            update("expenditure")
        elif(terminal_input == "help"):
            op.tab_print(OUTPUT, 0, "show, insert, delete, rexp, back")
        else:
            op.tab_print(OUTPUT, 0, "command not found")

        op.home(post = ZERO)
        op.expenditure_intro(post = INPUT)
        terminal_input = input()

def recurring_expenditure_terminal():
    op.home(post = ZERO)
    op.expenditure_intro()
    op.recurring_expenditure_intro(post = INPUT)
    terminal_input = input()
    while(terminal_input != "back"):
        if(terminal_input == "show"):
            table = dbi.select_table("recurring_expenditure")
            op.table(table, tabs = OUTPUT)
        elif(terminal_input == "insert"):
            insert("recurring_expenditure")
        elif(terminal_input == "delete"):
            delete("recurring_expenditure")
        elif(terminal_input == "update"):
            update("recurring_expenditure")
        elif(terminal_input == "help"):
            op.tab_print(OUTPUT, 0, "show, insert, delete, back")
        else:
            op.tab_print(OUTPUT, 0, "command not found")


        op.home(post = ZERO)
        op.expenditure_intro()
        op.recurring_expenditure_intro(post = INPUT)
        terminal_input = input()

def news_terminal():
    op.home(post = ZERO)
    op.news_intro(post = INPUT)
    terminal_input = input()
    while(terminal_input != "back"):
        if(terminal_input == "keyw"):
            keywords_terminal()
        elif(terminal_input == "help"):
            op.tab_print(OUTPUT, 0, "keyw, back")
        else:
            op.tab_print(OUTPUT, 0, "command not found")
        
        op.home(post = ZERO)
        op.news_intro(post = INPUT)
        terminal_input = input()

def keywords_terminal():
    op.home(post = ZERO)
    op.news_intro()
    op.keywords_intro(post = INPUT)
    terminal_input = input()
    while(terminal_input != "back"):
        if(terminal_input == "show"):
            table = dbi.select_table("keywords")
            op.table(table, tabs = OUTPUT)
        elif(terminal_input == "insert"):
            insert("keywords")
        elif(terminal_input == "delete"):
            delete("keywords")
        elif(terminal_input == "update"):
            update("keywords")
        elif(terminal_input == "help"):
            op.tab_print(OUTPUT, 0, "show, insert, delete, back")
        else:
            op.tab_print(OUTPUT, 0, "command not found")
        
        op.home(post = ZERO)
        op.news_intro()
        op.keywords_intro(post = INPUT)
        terminal_input = input()

def incidents_terminal():
    op.home(post = ZERO)
    op.incidents_intro(post = INPUT)
    terminal_input = input()
    while(terminal_input != "back"):
        if(terminal_input == "show"):
            table = dbi.select_table("incidents")
            op.table(table, tabs = OUTPUT)
        elif(terminal_input == "delete"):
            delete("incidents")
        elif(terminal_input == "help"):
            op.tab_print(OUTPUT, 0, "show, delete, back")
        else:
            op.tab_print(OUTPUT, 0, "command not found")
        

        op.home(post = ZERO)
        op.incidents_intro(post = INPUT)
        terminal_input = input()

def university_terminal():
    op.home(post = ZERO)
    op.university_intro(post = INPUT)
    terminal_input = input()
    while(terminal_input != "back"):
        if(terminal_input == "show"):
            table = dbi.select_table("university")
            op.table(table, tabs = OUTPUT)
        elif(terminal_input == "insert"):
            insert("university")
        elif(terminal_input == "delete"):
            delete("university")
        elif(terminal_input == "update"):
            update("update")
        elif(terminal_input == "help"):
            op.tab_print(OUTPUT, 0, "show, insert, delete, back")
        else:
            op.tab_print(OUTPUT, 0, "command not found")

        op.home(post = ZERO)
        op.university_intro(post = INPUT)
        terminal_input = input()

#-------------------------------------------------------------------
#Inserts

insert_questions_dictionary = {
    "calendar":
    [
        ["name of new calendar entry (str):", str],
        ["day (int):", int],
        ["month (int):", int],
        ["year (int):", int]
    ],
    "mothersdays":
    [
        ["day of mothersday (int):", int],
        ["month (int):", int],
        ["year (int):", int]
    ],
    "fathersdays":
    [
        ["day of fathersday (int):", int],
        ["month (int):", int],
        ["year (int):", int]
    ],
    "birthdays":
    [
        ["full name of birthday boy/girl (str):", str],
        ["day (int):", int],
        ["month (int):", int],
        ["year (0, if unknown)(int):", int]
    ],
    "expenditure":
    [
        ["name of new expenditure (str):", str],
        ["day (int):", int],
        ["month (int):", int],
        ["year (int):", int],
        ["category (str):", str],
        ["amount (float):", float]
    ],
    "recurring_expenditure":
    [
        ["name of new recurring expenditure (str):", str],
        ["category (str):", str],
        ["start month (int):", int],
        ["start year (int):", int],
        ["end month (int):", int],
        ["end year (int):", int],
        ["amount (float):", float]
    ],
    "keywords":     
    [
        ["name of new keyword (str):", str],
        ["score (float):", float]
    ],
    "university":
    [
        ["name of new university entry (str):", str],
        ["day (int):", int],
        ["month (int):", int],
        ["year (int):", int]
    ]
}

insert_db_dictionary = {
    "calendar": dbi.insert_into_calendar,
    "mothersdays": dbi.insert_into_mothersdays,
    "fathersdays": dbi.insert_into_fathersdays,
    "birthdays": dbi.insert_into_birthdays,
    "expenditure": dbi.insert_into_expenditure,
    "recurring_expenditure": dbi.insert_into_recurring_expenditure,
    "keywords": dbi.insert_into_keywords,
    "university": dbi.insert_into_university
}

def insert(table_name):
    input_list = []
    for row in insert_questions_dictionary[table_name]:
        question = row[0]
        print("")
        op.tab_print(INPUT, INPUT, question)
        string = str(input())
        if(string == "back"):
            op.tab_print(OUTPUT, 0, "process aborted.")
            return
        try:
            row[1](string)
        except:
            op.tab_print(OUTPUT, 0, "incorrect type. process aborted.")
            return
        input_list.append(string)
    print("")
    op.tab_print(INPUT, 0, "insert following element? (yes/no)")
    op.table([input_list], INPUT)
    op.tab(INPUT)
    terminal_input = str(input())
    success = False
    if(terminal_input == "yes"):
        success = insert_db_dictionary[table_name](input_list)
    if(success):
        op.tab_print(OUTPUT, 0, "successfull insertion.")
        return
    else:
        op.tab_print(OUTPUT, 0, "proccess aborted.")
        return

#-------------------------------------------------------------------
#Updates

update_questions_dictionary = {
    "calendar":
    [
        ["name (str):", str],
        ["day (int):", int],
        ["month (int):", int],
        ["year (int):", int]
    ],
    "mothersdays":
    [
        ["day (int):", int],
        ["month (int):", int],
        ["year (int):", int]
    ],
    "fathersdays":
    [
        ["day (int):", int],
        ["month (int):", int],
        ["year (int):", int]
    ],
    "birthdays":
    [
        ["name (str):", str],
        ["day (int):", int],
        ["month (int):", int],
        ["year (0, if unknown)(int):", int]
    ],
    "expenditure":
    [
        ["name (str):", str],
        ["day (int):", int],
        ["month (int):", int],
        ["year (int):", int],
        ["category (str):", str],
        ["amount (float):", float]
    ],
    "recurring_expenditure":
    [
        ["name (str):", str],
        ["category (str):", str],
        ["start_month (int):", int],
        ["start_year (int):", int],
        ["end_month (int):", int],
        ["end_year (int):", int],
        ["amount (float):", float]
    ],
    "keywords":     
    [
        ["name (str):", str],
        ["score (float):", float]
    ],
    "university":
    [
        ["name (str):", str],
        ["day (int):", int],
        ["month (int):", int],
        ["year (int):", int]
    ]
}

def update(table_name):
    update_list = []
    print("")
    op.tab_print(INPUT, INPUT, "rowid of element (int):")
    rowid = str(input())
    try:
        int(rowid)
    except:
        op.tab_print(OUTPUT, 0, "incorrect type. process aborted.")
        return
    selection = create_selection(rowid, table_name)
    updated_selection = create_selection(rowid, table_name)
    print("")
    op.tab_print(INPUT, 0, "selected element:")
    op.table([selection], INPUT)
    op.tab_print(INPUT, 0, "enter new values for all changed attributes or leave blank.")
    iterator = 1
    for row in update_questions_dictionary[table_name]:
        question = row[0]
        print("")
        op.tab_print(INPUT, INPUT, question)
        string = str(input())
        if(not string == ""):
            if(string == "back"):
                op.tab_print(OUTPUT, 0, "process aborted.")
                return
            try:
                row[1](string)
            except:
                op.tab_print(OUTPUT, 0, "incorrect type. process aborted.")
                return
            update_list.append([row[0].split()[0], row[1](string)])
            updated_selection[iterator] = string
        iterator = iterator + 1
    print("")
    op.tab_print(INPUT, 0, "update element from the first to the second?(yes/no)")
    op.table([selection, updated_selection], INPUT)
    op.tab(INPUT)
    terminal_input = str(input())
    success = False
    if(terminal_input == "yes"):
        success = dbi.update_by_rowid(rowid, table_name, update_list)
    if(success):
        op.tab_print(OUTPUT, 0, "successfull update.")
        return
    else:
        op.tab_print(OUTPUT, 0, "proccess aborted.")
        return

def create_selection(rowid, table_name):
    fetch = dbi.select_by_rowid(rowid, table_name)
    if(len(fetch) == 0):
        return None
    selection = []
    for value in fetch[0]:
        selection.append(value)
    return selection

#-------------------------------------------------------------------
#Deletes

def delete(table_name):
    print("")
    op.tab_print(INPUT, INPUT, "rowid of element (int):")
    rowid = str(input())
    try:
        int(rowid)
    except:
        op.tab_print(OUTPUT, 0, "incorrect type. process aborted.")
        return
    print("")
    op.tab_print(INPUT, 0, "delete following element? (yes/no)")
    op.table(dbi.select_by_rowid(rowid, table_name), INPUT)
    op.tab(INPUT)
    terminal_input = input()
    if(terminal_input == "yes"):
        dbi.delete_by_rowid(rowid, table_name)
        op.tab_print(OUTPUT, 0, "successfull deletion.")
    else:
        op.tab_print(OUTPUT, 0, "proccess aborted.")



the_one_ring()