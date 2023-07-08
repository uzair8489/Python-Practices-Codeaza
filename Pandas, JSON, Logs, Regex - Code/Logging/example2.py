import logging
import time

# Configure logging
logging.basicConfig(filename='example2.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

num1 = 10
num2 = 0

try:
    start_time = time.time()

    if num2 == 0:
        logging.info('Dividing by zero may result in unexpected behavior')
    result = num1 / num2
    logging.info('Division successful: {} / {} = {}'.format(num1, num2, result))
    print('Result:', result)

    end_time = time.time()
    execution_time = end_time - start_time
    logging.info('Execution time: {} seconds'.format(execution_time))

except ZeroDivisionError:
    logging.error('Division by zero occurred')
    print('Error occurred during division')
