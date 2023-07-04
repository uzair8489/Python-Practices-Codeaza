#                                                          DATABASE INTEGRATION

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

#code to select all the data from the table i created named 'random'
cursor = connection.cursor()
cursor.execute("SELECT * FROM random")
result = cursor.fetchall()
for rows in result:
    print(rows)

connection.close()


"""
The code establishes a connection to a MySQL database using mysql.connector, checks the connection status, selects all data from a
table named 'random', and prints the results. It demonstrates basic database integration in Python using MySQL.

"""