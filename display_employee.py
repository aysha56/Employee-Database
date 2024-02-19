import main as m
def display_employee(connection):
    print("                 --->>>> Display Employee Details <<<<----                        ")

    sql= 'select * from empdata'
    c = connection.cursor()
    c.execute(sql)
    r= c.fetchall()
    print("Number of count ", r)
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