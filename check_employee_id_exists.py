def employee_id_exists(id,connection):
    sql = "select * from empdata where id=%s"
    c = connection.cursor(buffered=True)
    data = (id,)
    c.execute(sql,data)
    count = c.rowcount
    # print("Employee Id  exists or not Count :", count)
    if count == 1:
        return True
    else:
        return False