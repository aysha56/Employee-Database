def employee_name_exists(name,connection):
    sql = "select * from empdata where name=%s"
    c = connection.cursor(buffered=True)
    data = (name,)
    c.execute(sql,data)
    count = c.rowcount
    # print("Employee Id  exists or not Count :", count)
    if count == 1:
        return True
    else:
        return False