import mysql.connector as connection
try:
    mydb = connection.connect(host="localhost", user="root", passwd="mysql", use_pure=True)
    print(mydb.is_connected())

    query = "CREATE DATABASE MYSQL_TABLES;"
    cursor = mydb.cursor()
    cursor.execute(query)
    print("Database Created!!")
    mydb.close()
except Exception as e:
    print(e)
