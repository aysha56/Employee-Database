

import mysql.connector
from os import system
import add_employee as add
import display_employee as display
import update_employee as update
import promote_employee as promote
import remove_employee as remove
import search_employee as search
def main_function(connection,):
    """print("This is my Main Function")
    print("My Data Base Created Successfully with the name : ", database_name)"""
    system("cls")
    print("*************************************************************************************")
    print("                         Employee Data Base Management                       ")
    print("*************************************************************************************")
    print("1: Add Employee to Data Base")
    print("2: Display Employee Data")
    print("3: Update Employee Data")
    print("4: Promote Employee Data")
    print("5: Remove Employee Data From Data Base")
    print("6: Search Employee Data")
    print("7: Exit\n")
    print("-------->>> Choose Choices: [1 2 3 4 5 6 7] <<<----------")
    choice = int(input("Enter choice : "))
    if choice == 1:
        system("cls")
        add.add_employee(connection)
        print("Add Employee Going to be Defined")
        print()
        #exit(0)
        main_function(connection)
    elif choice == 2:
        system("cls")
        display.display_employee(connection)
        print("Display Employee Going to be Defined")
        print()
        #exit(0)
        main_function(connection)
    elif choice == 3:
        system("cls")
        update.update_employee(id,connection)
        print("Update Employee Going to be Defined")
        print()
        #exit(0)
        main_function(connection)
    elif choice == 4:
        system("cls")
        promote.promote_employee(connection)
        print("Pramote Employee Going to be Defined")
        print()
        #exit(0)
        main_function(connection)
    elif choice == 5:
        system("cls")
        remove.remove_employee(connection)
        print("Remove Employee Going to be Defined")
        print()
        #exit(0)
        main_function(connection)
    elif choice == 6:
        system("cls")
        search.search_employee(connection)
        print("Search Employee Going to be Defined")
        print()
        #exit(0)
        main_function(connection)
    elif choice == 7:
        system("cls")
        print("Thank you for your patience Have a Nice day!!!")
        exit(0)
        #main_function()
    else:
        print("Invalid Choice Reason:\n   Choice not defined ", choice)
        click = input("     Press any key to continue further...")
        main_function(connection)


if __name__ == '__main__':
    print("                     --->>>Welcome to Employee Database Management System<<<<---                 ")
    username = input("Enter DB User Name : ")#User Name as Input from User
    password = input("Enter DB Password : ")#Password as Input from User
    try:
        connection = mysql.connector.connect(host="localhost", username=username, password= password)
    except:
        print("Entered password might be wrong, Please check...")
        exit(0)
    database_name = input("Enter Database Name : ")
    cur = connection.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS "+database_name)
    connection = mysql.connector.connect(host="localhost", username=username, password= password, database = database_name)
    cursur = connection.cursor()
    cursur.execute("CREATE TABLE IF NOT EXISTS empdata (Id INT(11) PRIMARY KEY, Name VARCHAR(1800), Email_Id Text(1800), Phone_no "
                   "BIGINT(11), Address TEXT(1000), Post TEXT(1000), Salary BIGINT(11))")
    main_function(connection)
