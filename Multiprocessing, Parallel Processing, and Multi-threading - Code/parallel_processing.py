import concurrent.futures
import time

def process_data(data):
    # Simulate processing time
    time.sleep(2)
    # Process the data here
    result = data.upper()
    return result

if __name__ == '__main__':
    data_list = ['apple', 'banana', 'cherry', 'date']  # List of data to process

    start_time = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Submit the tasks to the executor
        future_results = [executor.submit(process_data, data) for data in data_list]

        # Get the results as they become available
        for future in concurrent.futures.as_completed(future_results):
            try:
                result = future.result()
                print(f"Processed data: {result}")
            except Exception as e:
                print(f"An error occurred: {e}")

    # All tasks have been completed
    end_time = time.perf_counter()
    print("All tasks completed.")

    print(f'Total Execution Time: {end_time - start_time:.2f} seconds')
