import mysql.connector as connection

try:
    mydb = connection.connect(host="localhost", user="root1", passwd="mysql", use_pure=True)
    # check if the connection is established
    print(mydb.is_connected())
    mydb.close()
except Exception as e:
    print(e)