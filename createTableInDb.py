import mysql.connector as connection

try:
    mydb = connection.connect(host="localhost", database="MYSQL_TABLES" ,user="root", passwd="mysql", use_pure=True)
    print(mydb.is_connected())
    cursor = mydb.cursor()
    query = "CREATE TABLE StudentDetails( StudentID INT(10) PRIMARY KEY, First_Name Varchar(50), " \
            "Last_Name varchar(50), JoinDate DATE, Class Varchar(20), Section varchar(1) )"
    cursor.execute(query)
    print("Table Created!!")
    mydb.close()
except Exception as e:
    print(e)