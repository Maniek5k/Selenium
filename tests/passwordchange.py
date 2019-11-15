from variables import *

start_time = time.time()

print(colored("TEST STARTED: Login & logout \nStart: Go to test website", "green", attrs=['bold']))
driver.get(website)

print("1: Click login button")
driver.find_element_by_xpath(login_btn).click()

print("2: Fill login form with email and password")
driver.find_element_by_xpath(login_mail).send_keys(change_password_email)
driver.find_element_by_xpath(login_pwd).send_keys(default_password)

print("3: Click submit button")
driver.find_element_by_xpath(login_submit).click()

print("4: Checking for current URL")
if driver.current_url == account_page:
    print(colored("Login was successful", "blue"))
else:
    print("Error occurred")

print("5: Clicking account information CTA")
driver.find_element_by_class_name(change_password_info).click()

print("6: Sending current password")
driver.find_element_by_xpath(change_password_current).send_keys(default_password)

print("7: Sending newly generated password + confirming it")
driver.find_element_by_xpath(change_password_confirm).send_keys(new_password)
driver.find_element_by_xpath(change_password_new).send_keys(new_password)
print(colored("New password is: "+new_password, "yellow"))

print("8: Clicking save CTA")
driver.find_element_by_name(change_password_save).click()

print("CHECK: Checking for correct success message")
change_password_success = driver.find_element_by_xpath(change_password_alert).text
if change_password_success == change_password_success_text:
    print(colored("SUCCESS: Password changed correctly", "blue"))
else:
    print("Error occurred")

print("9: Logging out")
driver.find_element_by_xpath(logout_btn).click()

driver.implicitly_wait(5)
print("10: Checking correct log-out")
if driver.current_url == change_password_logout_page:
    print(colored("SUCCESS: Logout was successful", "blue"))
else:
    print("Error occurred")

print("11: Fill login form with email and changed password")
driver.find_element_by_xpath(login_mail).send_keys(change_password_email)
driver.find_element_by_xpath(login_pwd).send_keys(new_password)

print("12: Click submit button")
driver.find_element_by_xpath(login_submit).click()

print("13: Checking for current URL")
if driver.current_url == account_page:
    print(colored("Login was successful", "blue"))
else:
    print("Error occurred")

print("14: Clicking account information CTA")
driver.find_element_by_class_name(change_password_info).click()

print("15: Sending current password")
driver.find_element_by_xpath(change_password_current).send_keys(new_password)

print("16: Sending newly generated password + confirming it")
driver.find_element_by_xpath(change_password_confirm).send_keys(default_password)
driver.find_element_by_xpath(change_password_new).send_keys(default_password)
print(colored("New password is: "+str(default_password), "yellow"))

print("17: Clicking save CTA")
driver.find_element_by_name(change_password_save).click()

print("CHECK: Checking for correct success message")
change_password_success = driver.find_element_by_xpath(change_password_alert).text
if change_password_success == change_password_success_text:
    print(colored("SUCCESS: Password changed correctly", "blue"))
else:
    print("Error occurred")

print("18: Logging out")
driver.find_element_by_xpath(logout_btn).click()

driver.implicitly_wait(5)
print("19: Checking correct log-out")
if driver.current_url == change_password_logout_page:
    print(colored("SUCCESS: Logout was successful", "blue"))
    driver.close()
    print(colored("TEST FINISHED SUCCESSFULLY", "green", attrs=['bold']))
else:
    print("Error occurred")

end_time = time.time()
print(colored("Total execution time: {:0.2f} seconds".format(end_time - start_time), "cyan"))