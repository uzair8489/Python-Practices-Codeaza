#                                                        READ OPERATION

import mysql.connector

#setting up the connection script
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='lakeview',
    database='first_api_db'
)

#checking if the database is connected
if connection.is_connected():
    print('Database is connected successfully.\n')

    cursor = connection.cursor() 
    read_query = "select * from workers_data"
    cursor.execute(read_query)
    records = cursor.fetchall()
    # Displaying the retrieved records
    print("Workers Data: ")
    for record in records:
        print(record)
    

    # Closing the connection
    connection.close()

else:
    print("Errors connecting to database")
    connection.close()