#                                                        DELETE OPERATION

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
    delete_query = "delete from workers_data where id ='3'"
    cursor.execute(delete_query)
    
    connection.commit()    

    print("Data Deleted Successfully.")

    # Closing the connection
    connection.close()

else:
    print("Errors connecting to database")
    connection.close()