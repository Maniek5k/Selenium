from variables import *

start_time = time.time()

print(colored("TEST STARTED: Recover a forgotter password \nStart: Go to test website", "green", attrs=['bold']))
driver.get(website)

print("1: Go to login page - clicking button")
driver.find_element_by_xpath(login_btn).click()

print("2: Going to password recovery page")
driver.find_element_by_xpath(recover_password).click()

print("3: Providing e-mail address for password recovery")
driver.find_element_by_xpath(recover_email).send_keys(login_email)

print("4: Confirming password recovery")
driver.find_element_by_xpath(recover_confirm).click()

print("CHECK: Checking for correct success message")
password_success = driver.find_element_by_xpath(recover_success).text

if password_success == recover_success_text:
    print(colored("SUCCESS: Password reset email was correctly sent", "blue"))
    driver.close()
    print(colored("TEST FINISHED SUCCESSFULLY", "green", attrs=['bold']))
else:
    print("Error occurred")

end_time = time.time()
print(colored("Total execution time: {:0.2f} seconds".format(end_time - start_time), "cyan"))