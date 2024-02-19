import re
import main as m
import check_employee_id_exists as emp_exists
import employee_name_exists as emp_name

ph_num = re.compile("(0|91|)?[6-9][0-9]{9}")
def add_employee(connection):
    print("                 --->>>> Add Employee Details into Database <<<<----                        ")
    id = input("enter Employee Id : ")
    id_regex = '[0-9]{4}'
    if re.fullmatch(id_regex,id) is not None:
        print("valid Employee Id...")
        if emp_exists.employee_id_exists(id,connection):
            print("Employee Id already exists \n    Please try again.....")
            click = input("     Press any key to continue further...")
            add_employee(connection)
    else:
        print("Invalid Employee id and it Shouls be 5 digits from 0 to 9")
        add_employee(connection)
    name = input("Enter Employee Name : ")
    if emp_name.employee_name_exists(name, connection):
        print("Employee name already exists \n    Please try again.....")
        click = input("     Press any key to continue further...")
        add_employee(connection)
    email_id = input("Enter Employee Email Id : ")
    if re.fullmatch("\w*@{1}gmail\.com", email_id) is not None:
        print("      valid Email Id...   ")
    else:
        print("     Invalid Email Id...   ")
        click = input("     Press any key to continue further...")
        add_employee(connection)
    ph_no = input("Enter Employee Phone Number : ")
    if ph_num.match(ph_no):
        print("      valid Phone Number...   ")
    else:
        print("      Invalid Phone Number...   ")
        click = input("     Press any key to continue further...")
        add_employee(connection)
    address = input("Enter Employee Address : ")
    post = input("Enter Employee post Address : ")
    salary = input("Enter Employee Salary : ")
    employee_data = (id, name, email_id, ph_no, address, post, salary)
    sql_query = 'insert into empdata values(%s,%s,%s,%s,%s,%s,%s)'
    c = connection.cursor()
    c.execute(sql_query, employee_data)
    connection.commit()
    print("Employee Added Successfully into Employee Record.")
    click = input("Press any key to continue further....")
    m.main_function(connection)



