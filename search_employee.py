import main as m
import check_employee_id_exists as emp_exists
def  search_employee(connection):
    print("                 --->>>> Search Employee Details <<<<----                        ")
    id = input("enter Employee Id : ")
    if not emp_exists.employee_id_exists(id, connection):
        print(" Employee Id not exists \n    Please try again.....")
        click = input("     Press any key to continue further...")
        search_employee(connection)
    else:
        sql = 'select * from empdata where Id = %s'
        data = (id,)
        c = connection.cursor()
        c.execute(sql, data)
        r = c.fetchall()
        print("Employee found \n Employee Details....")
        for i in r:
            print("Employee Id: ", i[0])
            print("Employee Name : ", i[1])
            print("Employee Email Id : ", i[2])
            print("Employee Phone Number : ", i[3])
            print("Employee Address:", i[4])
            print("Employee Post: ", i[5])
            print("Employee Salary : ", i[6])
            print("\n")
        click = input("   Press any key to continue further...")
        m.main_function(connection)