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

def calendar_terminal():
    pass

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
            expenditure_delete()
        elif(terminal_input == "rexp"):
            recurring_expenditure_terminal()
        elif(terminal_input == "help"):
            op.tab_print(OUTPUT, 0, "show, insert, delete, rexp, back")
        else:
            op.tab_print(OUTPUT, 0, "command not found")
        

        op.home(post = ZERO)
        op.expenditure_intro(post = INPUT)
        terminal_input = input()

def expenditure_insert():
    new_exp = []
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
        new_exp.append(string)
    print("")
    op.tab_print(INPUT, 0, "insert following expenditure? (yes/no)")
    op.table([new_exp], INPUT)
    op.tab(INPUT)
    terminal_input = str(input())
    success = False
    if(terminal_input == "yes"):
        success = db.insert_into_expenditure( new_exp[0], 
                                    new_exp[1], 
                                    new_exp[2], 
                                    new_exp[3], 
                                    new_exp[4], 
                                    new_exp[5])
    if(success):
        op.tab_print(OUTPUT, 0, "successfull insertion.")
        return
    else:
        op.tab_print(OUTPUT, 0, "proccess aborted.")
        return

def expenditure_delete():
    print("")
    op.tab_print(INPUT, INPUT, "rowid of expenditure (int):")
    rowid = str(input())
    try:
        int(rowid)
    except:
        op.tab_print(OUTPUT, 0, "incorrect type. process aborted.")
        return
    print("")
    op.tab_print(INPUT, 0, "delete following expenditure? (yes/no)")
    op.table(db.select_by_rowid(rowid, "expenditure"), INPUT)
    op.tab(INPUT)
    terminal_input = input()
    if(terminal_input == "yes"):
        db.delete_by_rowid(rowid, "expenditure")
        op.tab_print(OUTPUT, 0, "successfull deletion.")
    else:
        op.tab_print(OUTPUT, 0, "proccess aborted.")

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
            recurring_expenditure_delete()
        elif(terminal_input == "help"):
            op.tab_print(OUTPUT, 0, "show, insert, delete, back")
        else:
            op.tab_print(OUTPUT, 0, "command not found")


        op.home(post = ZERO)
        op.expenditure_intro()
        op.recurring_expenditure_intro(post = INPUT)
        terminal_input = input()

def recurring_expenditure_insert():
    new_exp = []
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
        new_exp.append(string)
    print("")
    op.tab_print(INPUT, 0, "insert following recurring expenditure? (yes/no)")
    op.table([new_exp], INPUT)
    op.tab(INPUT)
    terminal_input = str(input())
    success = False
    if(terminal_input == "yes"):
        success = db.insert_into_recurring_expenditure( new_exp[0], 
                                                        new_exp[1], 
                                                        new_exp[2], 
                                                        new_exp[3], 
                                                        new_exp[4], 
                                                        new_exp[5],
                                                        new_exp[6])
    if(success):
        op.tab_print(OUTPUT, 0, "successfull insertion.")
        return
    else:
        op.tab_print(OUTPUT, 0, "proccess aborted.")
        return

def recurring_expenditure_delete():
    print("")
    op.tab_print(INPUT, INPUT, "rowid of recurring expenditure (int):")
    rowid = str(input())
    try:
        int(rowid)
    except:
        op.tab_print(OUTPUT, 0, "incorrect type. process aborted.")
        return
    print("")
    op.tab_print(INPUT, 0, "delete following recurring expenditure? (yes/no)")
    op.table(db.select_by_rowid(rowid, "recurring_expenditure"), INPUT)
    op.tab(INPUT)
    terminal_input = input()
    if(terminal_input == "yes"):
        db.delete_by_rowid(rowid, "recurring_expenditure")
        op.tab_print(OUTPUT, 0, "successfull deletion.")
    else:
        op.tab_print(OUTPUT, 0, "proccess aborted.")

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
            keyword_delete()
        elif(terminal_input == "help"):
            op.tab_print(OUTPUT, 0, "show, insert, delete, back")
        else:
            op.tab_print(OUTPUT, 0, "command not found")
        
        op.home(post = ZERO)
        op.news_intro()
        op.keywords_intro(post = INPUT)
        terminal_input = input()

def keyword_insert():
    new_exp = []
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
        new_exp.append(string)
    print("")
    op.tab_print(INPUT, 0, "insert following keyword? (yes/no)")
    op.table([new_exp], INPUT)
    op.tab(INPUT)
    terminal_input = str(input())
    success = False
    if(terminal_input == "yes"):
        success = db.insert_into_keywords(  new_exp[0], 
                                            new_exp[1])
    if(success):
        op.tab_print(OUTPUT, 0, "successfull insertion.")
        return
    else:
        op.tab_print(OUTPUT, 0, "proccess aborted.")
        return

def keyword_delete():
    print("")
    op.tab_print(INPUT, INPUT, "rowid of keyword (int):")
    rowid = str(input())
    try:
        int(rowid)
    except:
        op.tab_print(OUTPUT, 0, "incorrect type. process aborted.")
        return
    print("")
    op.tab_print(INPUT, 0, "delete following keyword? (yes/no)")
    op.table(db.select_by_rowid(rowid, "keywords"), INPUT)
    op.tab(INPUT)
    terminal_input = input()
    if(terminal_input == "yes"):
        db.delete_by_rowid(rowid, "keywords")
        op.tab_print(OUTPUT, 0, "successfull deletion.")
    else:
        op.tab_print(OUTPUT, 0, "proccess aborted.")

def incidents_terminal():
    op.home(post = ZERO)
    op.incidents_intro(post = INPUT)
    terminal_input = input()
    while(terminal_input != "back"):
        if(terminal_input == "show"):
            table = db.select_table("incidents")
            op.table(table, tabs = OUTPUT)
        elif(terminal_input == "delete"):
            incidents_delete()
        elif(terminal_input == "help"):
            op.tab_print(OUTPUT, 0, "show, delete, back")
        else:
            op.tab_print(OUTPUT, 0, "command not found")
        

        op.home(post = ZERO)
        op.incidents_intro(post = INPUT)
        terminal_input = input()

def incidents_delete():
    print("")
    op.tab_print(INPUT, INPUT, "rowid of incidence (int):")
    rowid = str(input())
    try:
        int(rowid)
    except:
        op.tab_print(OUTPUT, 0, "incorrect type. process aborted.")
        return
    print("")
    op.tab_print(INPUT, 0, "delete following incidence? (yes/no)")
    op.table(db.select_by_rowid(rowid, "incidents"), INPUT)
    op.tab(INPUT)
    terminal_input = input()
    if(terminal_input == "yes"):
        db.delete_by_rowid(rowid, "incidents")
        op.tab_print(OUTPUT, 0, "successfull deletion.")
    else:
        op.tab_print(OUTPUT, 0, "proccess aborted.")



the_one_ring()