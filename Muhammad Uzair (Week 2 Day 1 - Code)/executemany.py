#                                                        EXECUTEMANY OPERATION

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
    print('Database is connected successfully.')

    cursor = connection.cursor() 

    insert_data_query = """
    INSERT INTO workers_data (name, age, department) VALUES (%s, %s, %s)
    """

    # Inserting data into the table
    data = [
        ("Ahad", 30, "Sales"),
        ("Sufyan", 35, "Marketing"),
        ("Farooq", 28, "IT")
    ]
    cursor.executemany(insert_data_query, data)

    # Commit the changes
    connection.commit()

    print("Data inserted successfully.")

    # Closing the connection
    connection.close()

else:
    print("Errors connecting to database")
    connection.close()