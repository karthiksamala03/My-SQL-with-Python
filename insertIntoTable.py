import mysql.connector as connection

try:
    mydb = connection.connect(host="localhost", database="MYSQL_TABLES" ,user="root", passwd="mysql", use_pure=True)
    print(mydb.is_connected())
    cursor = mydb.cursor()
    query = "INSERT INTO studentdetails values(1, 'Raja', 'Ram', '2002-02-01', 'Tenth', 'A') "
    cursor.execute(query)
    query = "INSERT INTO studentdetails values(2, 'Pawan', 'Kalyan', '1997-02-01', 'Btech', 'A') "
    cursor.execute(query)
    print("Records Inserted!!")
    mydb.commit()
    mydb.close()
except Exception as e:
    print(e)