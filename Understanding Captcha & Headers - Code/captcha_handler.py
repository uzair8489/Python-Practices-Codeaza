import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

# Instantiate the WebDriver (e.g., ChromeDriver)
url = "https://nims.nadra.gov.pk/nims/registration"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)


# Navigate to a webpageinput
driver.get(url)


# Define the scroll height and increment value
scroll_height = 0
scroll_increment = 20
scroll_delay = 0.05  # Adjust the delay value for your desired scrolling speed

# Slowly scroll down the page
while scroll_height <= 600:
    driver.execute_script(f"window.scrollTo(0, {scroll_height});")
    scroll_height += scroll_increment
    time.sleep(scroll_delay)


answer_input = driver.find_element("xpath", "//input[@class='submit__input']")

captcha_answer = input("Enter the number: ")

time.sleep(2)

answer_input.send_keys(captcha_answer)

send_input = driver.find_element("xpath", "//input[@id='Form:chechEligBtn']")

send_input.click()


# Close the browser
# driver.quit()