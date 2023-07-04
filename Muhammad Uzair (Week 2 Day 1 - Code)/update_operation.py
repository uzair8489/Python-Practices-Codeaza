#                                                        UPDATE OPERATION

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
    read_query = "Update workers_data set age = '25' where id ='1'"
    cursor.execute(read_query)
    # Displaying the retrieved records
    print("Data updated successfully. ")
    

    connection.commit()
    # Closing the connection
    connection.close()

else:
    print("Errors connecting to database")
    connection.close()