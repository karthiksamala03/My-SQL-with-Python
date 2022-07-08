import mysql.connector as connection
try:
    mydb = connection.connect(host="localhost", user="root", passwd="mysql", use_pure=True)

    query = "SHOW DATABASES;"
    # Creating cursor
    cursor = mydb.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)
    for i in result:
        print(i)
    mydb.close()
except Exception as e:
    print(e)