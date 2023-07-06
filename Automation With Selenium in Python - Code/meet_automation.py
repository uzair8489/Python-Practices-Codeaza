import time
from selenium import webdriver
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
    driver.get('https://apps.google.com/intl/en/meet/')

    # Scroll the window by 200 pixels
    driver.execute_script("window.scrollBy(0,200)")

    # Find the "Join Meeting" element
    join_meeting_element = driver.find_element("xpath", "//div[@class='join_meeting_widget']")

    # Add a delay for stability
    time.sleep(3)

    # Find the "Meeting Code" input field
    meet_code_field = join_meeting_element.find_element("xpath", "./input[@class='glue-caption']")

    # Enter the meeting code in the input field
    meet_code_field.send_keys("ecm-okyf-ofm")

    time.sleep(2)

    # Find the "Join" button
    join_button = join_meeting_element.find_element("xpath", "./a/button")

    join_button.click()

except Exception as e:
    print("Error: ", e)

