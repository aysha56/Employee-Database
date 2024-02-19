import main as m
import check_employee_id_exists as emp_exists

def promote_employee(connection):
    """promote employee considering only salary"""
    print("                 --->>>> Promote Employee Details <<<<----                        ")
    id = input("enter Employee Id : ")
    if  not emp_exists.employee_id_exists(id, connection):
        print("Employee Id already exists \n    Please try again.....")
        click = input("     Press any key to continue further...")
        promote_employee(connection)
    else:
        print("1: Software Engineer")
        print("2: Software  Associate Engineer")
        print("3: Senior Software Engineer")
        print("4: Technical Software Engineer")
        print("5: Technical Lead")
        print("1: Project Manager")
        designation_choice = int(input("Enter Designation choice : "))
        if designation_choice == 1:
            print("Choice 1 is Software Engineer and max Increment is 1500/- are you sure want to promote : Yes/No ")
            confirmation = input("Please Enter your Confirmation : ")
            confirmation.lower()
            amount = 1500
        elif designation_choice == 2:
            print("Choice 2 is Software Associate Engineer and max Increment is 2000/- are you sure want to promote : Yes/No ")
            confirmation = input("Please Enter your Confirmation : ")
            confirmation.lower()
            amount = 2000
        elif designation_choice == 3:
            print("Choice 3 is Senior Software Engineer and max Increment is 4000/- are you sure want to promote : Yes/No ")
            confirmation = input("Please Enter your Confirmation : ")
            confirmation.lower()
            amount = 4000
        elif designation_choice == 4:
            print("Choice 4 is Technical Software Engineer and max Increment is 3000/- are you sure want to promote : Yes/No ")
            confirmation = input("Please Enter your Confirmation : ")
            confirmation.lower()
            amount = 3000
        elif designation_choice == 5:
            print("Choice 5 is Technical Lead and max Increment is 5000/- are you sure want to promote : Yes/No ")
            confirmation = input("Please Enter your Confirmation : ")
            confirmation.lower()
            amount = 5000
        elif designation_choice == 6:
            print("Choice 6 is Project Manager and max Increment is 7000/- are you sure want to promote : Yes/No ")
            confirmation = input("Please Enter your Confirmation : ")
            confirmation.lower()
            amount = 7000
        else:
            promote_employee(connection)


        # amount = int(input("Enter Empoyee Salary to increase : "))
        sql = 'select Salary from empdata where Id = %s'
        data = (id,)
        c = connection.cursor()
        c.execute(sql, data)
        #fetch current salary of employee
        s = c.fetchone()
        print("Current Salary : ",s)
        i = s[0]+amount
        print("Increased Salary : ",i )
        psql = 'UPDATE empdata set Salary = %s where Id = %s'
        d = (i,id,)
        c.execute(psql,d)
        connection.commit()
        print("Employee Salary is Successfully Promoted into Employee Record.")
        click = input("Press any key to continue further....")
        m.main_function(connection)
