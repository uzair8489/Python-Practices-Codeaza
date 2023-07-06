import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

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
    driver.get('https://www.youtube.com/')


    # Find the "Join Meeting" element
    search_input = driver.find_element("xpath", "//input[@id='search']")

    # Add a delay for stability
    time.sleep(2)

    # Enter the query in the input field
    search_input.send_keys("selenium automation")

    time.sleep(2)

    # Find the search button
    search_button = driver.find_element("xpath", "//button[@id='search-icon-legacy']")

    search_button.click()

except Exception as e:
    print("Error: ", e)

