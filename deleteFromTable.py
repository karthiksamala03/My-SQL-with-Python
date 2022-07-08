import mysql.connector as connection

try:
    mydb = connection.connect(host="localhost", database="MYSQL_TABLES" ,user="root", passwd="mysql", use_pure=True)
    print(mydb.is_connected())
    cursor = mydb.cursor()
    query = "DELETE FROM studentdetails WHERE studentid = 1 "
    cursor.execute(query)
    print("Records Deleted!!")
    mydb.commit()
    mydb.close()
except Exception as e:
    print(e)