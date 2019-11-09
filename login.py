from variables import *

start_time = time.time()

print("TEST STARTED: Login \nStart: Go to test website")
driver.get(website)

print("1: Click login button")
driver.find_element_by_xpath(login_btn).click()

print("2: Fill login form with email and password")
driver.find_element_by_xpath(login_mail).send_keys(login_email)
driver.find_element_by_xpath(login_pwd).send_keys(login_password)

print("3: Click submit button")
driver.find_element_by_xpath(login_submit).click()

print("4: Checking for current URL")
if driver.current_url == account_page:
    print("Login was successful")
else:
    print("Error occurred")

print("5: Logging out")
driver.find_element_by_xpath(logout_btn).click()

print("6: Checking correct log-out")
if driver.current_url == login_page:
    print("SUCCESS: Logout was successful")
    driver.close()
    print("TEST FINISHED SUCCESSFULLY")
else:
    print("Error occurred")

end_time = time.time()
print("Total execution time: {:0.2f} seconds".format(end_time - start_time))