#                                                          CREATE OPERATION

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


    # creating a new table
    create_table_query = """
    CREATE TABLE workers_data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        age INT,
        department VARCHAR(100)
    )
    """ 

    insert_data_query = """
    INSERT INTO workers_data (name, age, department) VALUES ("Uzair", 25, "IT")
    """
    # Execute the create table query
    cursor.execute(create_table_query)
    print("Table Created Successfuly\n")
    cursor.execute(insert_data_query)
    print("Data inserted Successfuly\n")


    # Commit the changes
    connection.commit()

    # Closing the connection
    connection.close()

else:
    print("Errors connecting to database")
    connection.close()


"""
The code establishes a connection to a MySQL database using mysql.connector, checks the connection status, creates a table in
the database naming 'workers_data' and then inserts the data in the table a and prints the results. It demonstrates basic database
integration in Python using MySQL.

"""