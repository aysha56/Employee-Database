import re
import main as m
import check_employee_id_exists as emp_exists
import add_employee
def update_employee(id,connection):
    print("                 --->>>> Update Employee Details <<<<----                        ")
    id = input("enter Employee Id : ")
    if emp_exists.employee_id_exists(id, connection) == False:
        print("Employee Id already exists \n    Please try again.....")
        click = input("     Press any key to continue further...")
        update_employee(connection)
    else:
        email_id = input("Enter Employee Email Id : ")
        if re.fullmatch("\w*@{1}gmail\.com", email_id) is not None:
            print(" Valid Email Id....")
        else:
            print(" Invalid Email Id...." )
            click = input("Press any key to continue further...")
            update_employee(connection)
    phone_no = input("Enter Employee Phone Number : ")
    if add_employee.ph_num.match(phone_no):
        print("Valid Phone Number....")
    else:
        print(" Invalid Email Id.... ")
        click = input("     Press any key to continue further...")
        update_employee(connection)
    address = input("Enter Employee Address : ")
    sql = 'UPDATE empdata set Email_ID = %s,Phone_no = %s,Address = %s where Id = %s'
    data = (email_id,phone_no,address,id,)
    c = connection.cursor()
    c.execute(sql,data)
    connection.commit()
    print("Employee Details are Updated Successfully into Employee Record.")
    click = input("Press any key to continue further....")
    m.main_function(connection)


