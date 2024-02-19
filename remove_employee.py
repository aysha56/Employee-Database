import main as m
import check_employee_id_exists as emp_exists

def remove_employee(connection):
    print("                 --->>>> Remove Employee Details <<<<----                        ")
    id = input("enter Employee Id : ")
    if not emp_exists.employee_id_exists(id, connection):
        print("Employee Id already exists \n    Please try again.....")
        click = input("     Press any key to continue further...")
        m.main_function(connection)
    else:
        sql = 'delete from empdata  where Id = %s'
        data = (id,)
        c = connection.cursor()
        c.execute(sql, data)
        connection.commit()
        print("Employee Details Removed Successfully from Employee Record.")
        click = input("Press any key to continue further....")
        m.main_function(connection)
