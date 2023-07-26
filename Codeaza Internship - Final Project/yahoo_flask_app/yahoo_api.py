import logging
import os
import mysql.connector
import pandas as pd
from mysql.connector import Error
from flask import Flask, jsonify
import subprocess

app = Flask(__name__)
app.json.sort_keys = False


# Configure logging
logging.basicConfig(filename='yahoo_api.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/', methods=['GET'])
def home():
    return 'Welcome to the Yahoo Finance Data API!'

@app.route('/fetch_data/', methods=['GET'])
def fetch_data():
    try:
        # Change the working directory to the Scrapy project folder
        scrapy_project_path = '../yahoo_scrapper'

        # Run the Scrapy spider as a subprocess
        process = subprocess.Popen(['scrapy', 'crawl', 'yahoo_finance'], cwd=scrapy_project_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()

        if err:
            # If there was an error in the Scrapy spider, read the log file and filter messages with ERROR level
            with open('../yahoo_scrapper/yahoo_spider.log', 'r') as log_file:
                log_lines = log_file.readlines()

            # Filter out the log messages with ERROR level
            error_messages = [line.strip() for line in log_lines if ' - ERROR - ' in line or ' - CRITICAL - ' in line]
            if error_messages:
                error_message = '\n'.join(error_messages)
                logging.error("An error occurred during spider execution")
                return jsonify({'Status Code' : 500,'Error' : 'An error occurred during spider execution. Check spider log file'}), 500



        # Return a response indicating success
        logging.info("Data fetched successfully")
        return jsonify({'Status Code' : 200, 'message': 'Data fetched successfully'}), 200

    except Exception as e:
        logging.error(f"Error during spider execution: {e}")
        # Handle any exceptions that may occur during spider execution
        return jsonify({'Error': f'Error: {e}'}), 500
    

# Define a route for the API endpoint
@app.route('/get-all-data/', methods=['GET'])
def get_all_data():
    try:
        connection = mysql.connector.connect(
            host=os.environ.get('YOUR_MYSQL_HOST'),
            user=os.environ.get('YOUR_MYSQL_USERNAME'),
            password=os.environ.get('YOUR_MYSQL_PASSWORD'),
            database=os.environ.get('YOUR_MYSQL_DATABASE')
        )

        if connection.is_connected():
            cursor = connection.cursor()

            logging.info('Retrieving the Data...')
            # Query to fetch all data from the table
            query = "SELECT * FROM yahoo_finance_data"
            cursor.execute(query)

            # Fetch all records
            records = cursor.fetchall()

            # Convert records to a list of dictionaries
            data = []
            for record in records:
                data.append({
                    'id' : record[0],
                    'symbol': record[1],
                    'name': record[2],
                    'last_price': str(record[3]),  # Convert Decimal to string
                    'change': record[4],
                    'change_percentage': record[5],
                    'timestamp': str(record[6]),  # Convert datetime to string
                })

            cursor.close()
            connection.close()

            # Return JSON response
            logging.info("Data retrieved successfully from the database")
            return jsonify(data)

    except Error as e:
        logging.error(f"Error fetching data from database: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
