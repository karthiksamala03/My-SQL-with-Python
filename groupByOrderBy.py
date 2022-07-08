import mysql.connector as connection
import pandas
import pandas as pd

try:
    mydb = connection.connect(host="localhost", user="root", passwd="mysql", database="mysql_tables", use_pure=True)
    # check if the connection is establis
    print(mydb.is_connected())
    # Create a glass table to store glass data
    query = "SELECT CLASS, SUM(RI),SUM(MG),SUM(AL) FROM mysql_tables.GLASSDATA GROUP BY CLASS ORDER BY CLASS;"
    result = pandas.read_sql(query,mydb)
    print(result)

    mydb.close()    # close the connection
except Exception as e:
    print(e)
