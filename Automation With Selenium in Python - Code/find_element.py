import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Initialize the Chrome webdriver
driver = webdriver.Chrome()

# Configure Chrome options
chrome_options = Options()

# Maximize the Chrome window
chrome_options.add_argument("--start-maximized")

# Keep the browser window open after the script finishes
chrome_options.add_experimental_option("detach", True)

# Create a new Chrome webdriver instance with the configured options
driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get('https://www.google.com')

    time.sleep(2)

    # Find the search input field using its name attribute
    search_input = driver.find_element(By.NAME, 'q')

    # Perform actions on the search input field
    search_input.send_keys('Selenium Automation')

    time.sleep(2)

    # Submit the search form
    search_input.submit()

    time.sleep(5)  # Wait for the search results to load

except Exception as e:
    print("Error: ", e)

finally:
    driver.quit()
