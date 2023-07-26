import scrapy
import pandas as pd
from datetime import datetime
import os
import mysql.connector
from mysql.connector import Error
import logging

class YahooFinanceSpider(scrapy.Spider):
    name = 'yahoo_finance'
    start_urls = ['https://finance.yahoo.com/lookup']

    # Clear the log file before configuring the logging
    with open('yahoo_spider.log', 'w'):
        pass

    # Configure logging after clearing the log file
    logging.basicConfig(filename='yahoo_spider.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def parse(self, response):
        # Configure logging

        # Find the table with the specified class
        table = response.xpath('//table[contains(@class, "trending-table")]')

        # Lists to store data
        symbols = []
        names = []
        last_prices = []
        changes = []
        change_percentages = []

        # Extract data from each row
        logging.info('Scrapping data....')
        for tr in table.xpath('.//tbody/tr'):
            symbols.append(tr.xpath('.//td[1]//a/text()').get())
            names.append(tr.xpath('.//td[2]/text()').get())
            last_prices.append(tr.xpath('.//td[3]/text()').get())
            changes.append(''.join(tr.xpath('.//td[4]//span/text()').getall()))
            change_percentages.append(''.join(tr.xpath('.//td[5]//span/text()').getall()))

        # Get the current timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Create DataFrame
        data = {
            'symbol': symbols,
            'name': names,
            'last_price': last_prices,
            'change': changes,
            'change_percentage': change_percentages,
            'timestamp': [timestamp] * len(symbols),  # Add timestamp to each row
        }


        # Save data to MySQL
        try:
            connection = mysql.connector.connect(
                host=os.environ.get('YOUR_MYSQL_HOST'),
                user=os.environ.get('YOUR_MYSQL_USERNAME'),
                password=os.environ.get('YOUR_MYSQL_PASSWORD'),
                database=os.environ.get('YOUR_MYSQL_DATABASE')
            )

            if connection.is_connected():
                logging.info('Database connected successfully....')
                cursor = connection.cursor()

                # save data in database
                logging.info('Inserting data into database...')
                for index, row in pd.DataFrame(data).iterrows():
                    query = "INSERT INTO yahoo_finance_data (symbol, name, last_price, change_value, change_percentage, timestamp) " \
                            "VALUES (%s, %s, %s, %s, %s, %s)"
                    values = (row['symbol'], row['name'], row['last_price'], row['change'], row['change_percentage'], row['timestamp'])
                    cursor.execute(query, values)

                connection.commit()
                logging.info(f"{len(data['symbol'])} records inserted into the MySQL database")

        except Error as e:
            logging.error(f"Error occured in database operations: {e}")
            raise  # Raise an exception to stop further execution

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                logging.info("MySQL connection is closed")

