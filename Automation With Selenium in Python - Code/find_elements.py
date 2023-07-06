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
    driver.get('https://www.google.com/en')
    
    # Find all link elements on the page
    link_elements = driver.find_elements(By.TAG_NAME, 'a')
    
    # Iterate over the link elements and print their text
    for link in link_elements:
        text = link.text
        print(text)

except Exception as e:
    print("Error: ", e)

finally:
    driver.quit()
