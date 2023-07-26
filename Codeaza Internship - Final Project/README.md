# Yahoo Finance Data API Documentation

## Introduction

The Yahoo Finance Data API is a web application that provides an API to fetch financial data from Yahoo Finance and store it in a MySQL database. The application is built using Python, Flask, Scrapy, and MySQL Connector.

## Requirements
To run this API, you need the following software installed:

1 Python
2 Flask
3 Scrapy
4 MySQL Connector/Python
5 Browser

Install the required Python packages by going into root directory of project and then using using pip.

pip install -r requirements.txt
The requirements.txt file contains a list of required Python packages along with their versions.

## Installation


The requirements.txt file contains a list of required Python packages along with their versions.

To set up the Yahoo Finance Data API on your local machine, follow these steps:


1. Install the required packages: `pip install -r requirements.txt`

2. Set up the MySQL database:
   - Create a new database: `CREATE DATABASE yahoo_api_db;`
   - Create the `yahoo_finance_data` table with the following schema:
     ```
     CREATE TABLE yahoo_finance_data (
       id INT AUTO_INCREMENT PRIMARY KEY,
       symbol VARCHAR(50),
       name VARCHAR(100),
       last_price VARCHAR(50),
       change_value VARCHAR(50),
       change_percentage VARCHAR(50),
       timestamp DATETIME
     );
     ```

3. Configure the database connection:

   - Update the `host`, `user`, `password`, and `database` variables with your MySQL database credentials.

4. Run the API by going into directory of yahoo_flask_app: `python yahoo_api.py`

## Usage

The Yahoo Finance Data API provides two endpoints:

1. `/fetch_data/`: This endpoint triggers the Scrapy spider to fetch data from Yahoo Finance and store it in the database.

2. `/get_all_data/`: This endpoint retrieves all the data from the `yahoo_finance_data` table and returns it in JSON format.

To use the API, make a GET request to the desired endpoint:

- Example usage for `/fetch_data/`:

GET http://localhost:5000/fetch_data/

- Example usage for `/get_all_data/`:

GET http://localhost:5000/get_all_data/


## Error Handling

If there is an error during the data fetching process, the API will return a JSON response with an error message. Additionally, the error details will be logged in the `yahoo_api.log` file.

And if there are errors during the scrapping of data in scrapy files, the error details will be logged in the 'yahoo_spider.log' file

## Conclusion

The Yahoo Finance Data API provides a simple and convenient way to fetch financial data from Yahoo Finance and store it in a MySQL database. It is built using popular Python libraries, making it easy to set up and use for various financial data retrieval applications.

## Note

- Ensure that you have a stable internet connection while using the `/fetch_data/` endpoint since it fetches data from Yahoo Finance.

- If you encounter any issues with the API, check the log file `yahoo_api.log` for error details.


---


