# filename: gitee_login_selenium.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Replace these with your actual Gitee account details
username = "13538774847"
password = "1415wsh52000"

# Initialize Chrome webdriver
driver = webdriver.Chrome()

# Open Gitee login page
driver.get("https://gitee.com/login")

# Find the username and password fields, fill them in
driver.find_element_by_name("user[login]").send_keys(username)
driver.find_element_by_name("user[password]").send_keys(password)

# Click the login button
driver.find_element_by_name("commit").click()

# Wait for the login process to finish
time.sleep(5)

# Close the browser
driver.quit()