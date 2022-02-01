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
        elif(terminal_input == "help"):
            op.tab_print(OUTPUT, 0, "cal, bir, exp, news, inc, stop")
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

#-------------------------------------------------------------------
#Inserts

questions_dictionary = {
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
    ]
}

insert_dictionary = {
    "calendar": dbi.insert_into_calendar,
    "mothersdays": dbi.insert_into_mothersdays,
    "fathersdays": dbi.insert_into_fathersdays,
    "birthdays": dbi.insert_into_birthdays,
    "expenditure": dbi.insert_into_expenditure,
    "recurring_expenditure": dbi.insert_into_recurring_expenditure,
    "keywords": dbi.insert_into_keywords
}

def insert(table_name):
    input_list = []
    for row in questions_dictionary[table_name]:
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
        success = insert_dictionary[table_name](input_list)
    if(success):
        op.tab_print(OUTPUT, 0, "successfull insertion.")
        return
    else:
        op.tab_print(OUTPUT, 0, "proccess aborted.")
        return

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