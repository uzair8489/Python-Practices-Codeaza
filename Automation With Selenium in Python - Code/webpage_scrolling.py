import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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
    driver.get('https://www.python.org/')

    time.sleep(2)

    # Scroll Down
    for _ in range(3): 
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(3)

    # Scroll Up
    for _ in range(3):
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_UP)

except Exception as e:
    print("Error: ", e)

finally:
    driver.quit()
