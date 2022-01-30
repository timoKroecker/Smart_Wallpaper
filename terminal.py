import output as op
import database_interface as db

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
            table = db.select_table("calendar")
            op.table(table, tabs = OUTPUT)
        elif(terminal_input == "insert"):
            calendar_insert()
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
            table = db.select_table("mothersdays")
            op.table(table, tabs = OUTPUT)
        elif(terminal_input == "insert"):
            mothersdays_insert()
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
            table = db.select_table("fathersdays")
            op.table(table, tabs = OUTPUT)
        elif(terminal_input == "insert"):
            fathersdays_insert()
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
    pass

def expenditure_terminal():
    op.home(post = ZERO)
    op.expenditure_intro(post = INPUT)
    terminal_input = input()
    while(terminal_input != "back"):
        if(terminal_input == "show"):
            table = db.select_table("expenditure")
            op.table(table, tabs = OUTPUT)
        elif(terminal_input == "insert"):
            expenditure_insert()
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
            table = db.select_table("recurring_expenditure")
            op.table(table, tabs = OUTPUT)
        elif(terminal_input == "insert"):
            recurring_expenditure_insert()
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
            table = db.select_table("keywords")
            op.table(table, tabs = OUTPUT)
        elif(terminal_input == "insert"):
            keyword_insert()
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
            table = db.select_table("incidents")
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

def calendar_insert():
    new = []
    questions =     [
                        ["name of new calendar entry (str):", str],
                        ["day (int):", int],
                        ["month (int):", int],
                        ["year (int):", int]
                    ]
    for row in questions:
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
        new.append(string)
    print("")
    op.tab_print(INPUT, 0, "insert following calendar entry? (yes/no)")
    op.table([new], INPUT)
    op.tab(INPUT)
    terminal_input = str(input())
    success = False
    if(terminal_input == "yes"):
        success = db.insert_into_calendar(  new[0], 
                                            new[1], 
                                            new[2], 
                                            new[3])
    if(success):
        op.tab_print(OUTPUT, 0, "successfull insertion.")
        return
    else:
        op.tab_print(OUTPUT, 0, "proccess aborted.")
        return

def mothersdays_insert():
    new = []
    questions =     [
                        ["day of mothersday (int):", int],
                        ["month (int):", int],
                        ["year (int):", int]
                    ]
    for row in questions:
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
        new.append(string)
    print("")
    op.tab_print(INPUT, 0, "insert following mothersday? (yes/no)")
    op.table([new], INPUT)
    op.tab(INPUT)
    terminal_input = str(input())
    success = False
    if(terminal_input == "yes"):
        success = db.insert_into_mothersdays(   new[0], 
                                                new[1], 
                                                new[2])
    if(success):
        op.tab_print(OUTPUT, 0, "successfull insertion.")
        return
    else:
        op.tab_print(OUTPUT, 0, "proccess aborted.")
        return

def fathersdays_insert():
    new = []
    questions =     [
                        ["day of fathersday (int):", int],
                        ["month (int):", int],
                        ["year (int):", int]
                    ]
    for row in questions:
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
        new.append(string)
    print("")
    op.tab_print(INPUT, 0, "insert following fathersday? (yes/no)")
    op.table([new], INPUT)
    op.tab(INPUT)
    terminal_input = str(input())
    success = False
    if(terminal_input == "yes"):
        success = db.insert_into_fathersdays(   new[0], 
                                                new[1], 
                                                new[2])
    if(success):
        op.tab_print(OUTPUT, 0, "successfull insertion.")
        return
    else:
        op.tab_print(OUTPUT, 0, "proccess aborted.")
        return

def expenditure_insert():
    new = []
    questions =     [
                        ["name of new expenditure (str):", str],
                        ["day (int):", int],
                        ["month (int):", int],
                        ["year (int):", int],
                        ["category (str):", str],
                        ["amount (float):", float]
                    ]
    for row in questions:
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
        new.append(string)
    print("")
    op.tab_print(INPUT, 0, "insert following expenditure? (yes/no)")
    op.table([new], INPUT)
    op.tab(INPUT)
    terminal_input = str(input())
    success = False
    if(terminal_input == "yes"):
        success = db.insert_into_expenditure( new[0], 
                                    new[1], 
                                    new[2], 
                                    new[3], 
                                    new[4], 
                                    new[5])
    if(success):
        op.tab_print(OUTPUT, 0, "successfull insertion.")
        return
    else:
        op.tab_print(OUTPUT, 0, "proccess aborted.")
        return

def recurring_expenditure_insert():
    new = []
    questions =     [
                        ["name of new recurring expenditure (str):", str],
                        ["category (str):", str],
                        ["start month (int):", int],
                        ["start year (int):", int],
                        ["end month (int):", int],
                        ["end year (int):", int],
                        ["amount (float):", float]
                    ]
    for row in questions:
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
        new.append(string)
    print("")
    op.tab_print(INPUT, 0, "insert following recurring expenditure? (yes/no)")
    op.table([new], INPUT)
    op.tab(INPUT)
    terminal_input = str(input())
    success = False
    if(terminal_input == "yes"):
        success = db.insert_into_recurring_expenditure( new[0], 
                                                        new[1], 
                                                        new[2], 
                                                        new[3], 
                                                        new[4], 
                                                        new[5],
                                                        new[6])
    if(success):
        op.tab_print(OUTPUT, 0, "successfull insertion.")
        return
    else:
        op.tab_print(OUTPUT, 0, "proccess aborted.")
        return

def keyword_insert():
    new = []
    questions =     [
                        ["name of new keyword (str):", str],
                        ["score (float):", float]
                    ]
    for row in questions:
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
        new.append(string)
    print("")
    op.tab_print(INPUT, 0, "insert following keyword? (yes/no)")
    op.table([new], INPUT)
    op.tab(INPUT)
    terminal_input = str(input())
    success = False
    if(terminal_input == "yes"):
        success = db.insert_into_keywords(  new[0], 
                                            new[1])
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
    op.table(db.select_by_rowid(rowid, table_name), INPUT)
    op.tab(INPUT)
    terminal_input = input()
    if(terminal_input == "yes"):
        db.delete_by_rowid(rowid, table_name)
        op.tab_print(OUTPUT, 0, "successfull deletion.")
    else:
        op.tab_print(OUTPUT, 0, "proccess aborted.")



the_one_ring()