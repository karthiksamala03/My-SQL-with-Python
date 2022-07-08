import mysql.connector as connection
import csv

try:
    mydb = connection.connect(host="localhost", user="root", passwd="mysql", database="mysql_tables", use_pure=True)
    print("Connection to database",end=" ")
    print(mydb.is_connected())

    # Create a glass table to store glass data
    query="CREATE TABLE IF NOT EXISTS GlassData (Index_Number INT(10),RI float(10,5), Na float(10,5), Mg float(10,5),Al float(10,5)," \
            " Si float(10,5), K float(10,5), Ca float(10,5), Ba float(10,5), Fe float(10,5), Class INT(5))"
    cursor = mydb.cursor()
    cursor.execute(query)
    print("Table Created!!")

    # inserting from file
    with open('glass.data',"r") as f:
        next(f)
        glass_data = csv.reader(f, delimiter='\n')
        for line in glass_data:
            #print(str(line[0]))
            cursor.execute("Insert into GlassData values( {values} )".format(values=str(line[0])))

    print("Records Inserted!!")
    mydb.commit()
    mydb.close()
except Exception as e:
    print(e)