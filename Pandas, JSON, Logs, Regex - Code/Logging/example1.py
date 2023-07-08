import logging

# Configure logging
logging.basicConfig(filename='example1.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

num1 = 10
num2 = 0

try:
    if num2 == 0:
        logging.critical('Dividing by zero may result in unexpected behavior')
        
    result = num1 / num2

    logging.info('Division successful: {} / {} = {}'.format(num1, num2, result))

    print('Result:', result)

except ZeroDivisionError:

    logging.error('Division by zero occurred')

    print('Error occurred during division')
