# filename: gitee_login.py
from drissionpage import Browser

# Initialize a browser
browser = Browser()

# Open Gitee login page
browser.get("https://gitee.com/login")

# Fill in the username and password fields
browser.find_element_by_name("input","name","form[login]", keys="13538774847")
browser.find_element_by_name("input","name","form[password]", keys="1415wsh52000")

# Click the login button
browser.find_element_by_css_selector("input[type=submit]").click()