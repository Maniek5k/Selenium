from test_data import *

start_time = time.time()

print(colored("TEST STARTED: Login & logout \nStart: Go to test website", "green", attrs=['bold']))
driver.get(website)

print("1: Click login button")
driver.find_element_by_xpath(login_btn).click()

print("2: Fill login form with email and password")
driver.find_element_by_xpath(login_mail).send_keys(login_email)
driver.find_element_by_xpath(login_pwd).send_keys(default_password)

print("3: Click submit button")
driver.find_element_by_xpath(login_submit).click()

print("4: Checking for current URL")
if driver.current_url == account_page:
    print(colored("Login was successful", "blue"))
else:
    print("Error occurred")

print("5: Logging out")
driver.find_element_by_xpath(logout_btn).click()

print("6: Checking correct log-out")
if driver.current_url == login_page:
    print(colored("SUCCESS: Logout was successful", "blue"))
    driver.close()
    print(colored("TEST FINISHED SUCCESSFULLY", "green", attrs=['bold']))
else:
    print("Error occurred")

end_time = time.time()
print(colored("Total execution time: {:0.2f} seconds".format(end_time - start_time), "cyan"))