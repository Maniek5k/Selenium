from variables import *

start_time = time.time()
driver.implicitly_wait(2)
print("TEST STARTED: Create new account\nStart: Go to test website")
driver.get(website)

print("1: Click sign in button")
driver.find_element_by_xpath(login_btn).click()

print("2: Sending new account email address ")
driver.find_element_by_xpath(create_acc_mail).send_keys(new_account_email)

print("3: Submitting account creation")
driver.find_element_by_xpath(create_acc_submit).click()

print("4: Choosing title")
driver.find_element_by_xpath(new_acc_radio).click()

print("5: Sending account owner first name")
driver.find_element_by_xpath(new_acc_first_name).send_keys("Tester new-acc")

print("6: Sending account owner last name")
driver.find_element_by_xpath(new_acc_last_name).send_keys("Tester lastname")

print("7: Sending account owner password")
driver.find_element_by_xpath(new_acc_password).send_keys("12345")

print("8: Sending first name - address")
driver.find_element_by_xpath(first_name).send_keys("Tester first")

print("9: Sending last name - address")
driver.find_element_by_xpath(last_name).send_keys('Tester last')

print("10: Sending company name")
driver.find_element_by_xpath(company).send_keys("Test company")

print("11: Sending address first line")
driver.find_element_by_xpath(address_1).send_keys("Test 1")

print("12: Sending address second line")
driver.find_element_by_xpath(address_2).send_keys("Test 2")

print("13: Sending city")
driver.find_element_by_xpath(city).send_keys("Test city")

print("14: Choosing state from list")
driver.find_element_by_xpath(state).click()

print("15: Sending zip code")
driver.find_element_by_xpath(zip_code).send_keys("00000")

print("16: Choosing country from list")
driver.find_element_by_xpath(country).click()

print("17: Sending mobile phone number")
driver.find_element_by_xpath(mobile_phone).send_keys("123123123")

print("18: Registering an account")
driver.find_element_by_xpath(new_acc_register).click()

print("CHECK: Checking for current URL")
if driver.current_url == account_page:
    print("Account created successfully")
else:
    print("Error occurred")

print("19: Logging out")
driver.find_element_by_xpath(logout_btn).click()

print("20: Checking correct data - logging into newly created account")
driver.find_element_by_xpath(login_mail).send_keys(new_account_email)
driver.find_element_by_xpath(login_pwd).send_keys(login_password)
driver.find_element_by_xpath(login_submit).click()

print("CHECK: Checking correct logging in")
if driver.current_url == account_page:
    print("SUCCESS: Login was successful")
    driver.find_element_by_xpath(logout_btn).click()
    print("TEST FINISHED SUCCESSFULLY")
    driver.close()
else:
    print("ERROR occured")

end_time = time.time()
print("Total execution time: {:0.2f} seconds".format(end_time - start_time))