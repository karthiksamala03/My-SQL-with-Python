import mysql.connector as connection
import pandas as pandas

try:
    mydb = connection.connect(host="localhost", database='mysql_tables', user="root", passwd="mysql", use_pure=True)
    # check if the connection is established
    print(mydb.is_connected())
    query = "UPDATE studentdetails SET First_Name = 'Kumar', Last_Name = 'Gaurav' WHERE Studentid = 2"
    cursor = mydb.cursor()  # create a cursor to execute queries
    cursor.execute(query)
    mydb.commit()

    #let's check if the value is updated in the table.
    query = "Select * from studentdetails where Studentid=2;"
    cursor = mydb.cursor()  # create a cursor to execute queries
    cursor.execute(query)
    for result in cursor.fetchall():
        print(result)

    mydb.close()  # close the connection

except Exception as e:
    #mydb.close()
    print(str(e))