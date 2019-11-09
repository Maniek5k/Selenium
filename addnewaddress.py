from variables import *

start_time = time.time()

print("TEST: Add new address\nStart: Go to test website")
driver.get(website)

print("1: Click login button")
driver.find_element_by_xpath(login_btn).click()

print("2: Fill login form with email and password")
driver.find_element_by_xpath(login_mail).send_keys(address_email)
driver.find_element_by_xpath(login_pwd).send_keys(address_pwd)

print("3: Click submit button")
driver.find_element_by_xpath(login_submit).click()

print("4: Checking for current URL")
if driver.current_url == account_page:
    print("4a: Login was successful")
else:
    print("Error occured")

print("5: Clicking address button")
driver.get(address_page)

print("5a: Checking if there are no addresses added to account")
address_removed = driver.find_element_by_xpath(no_addresses)
if address_removed.is_displayed():
    print("OK - no existing addresses found")
else:
    print("ERROR - there is anoether address, test terminated")

print("6: Clicking add new address button")
driver.find_element_by_xpath(add_new_address).click()

print("7: Sending first name")
driver.find_element_by_xpath(first_name).send_keys("Tester first")

print("8: Sending last name")
driver.find_element_by_xpath(last_name).send_keys('Tester last')

print("9: Sending company name")
driver.find_element_by_xpath(company).send_keys("Test company")

print("10: Sending address first line")
driver.find_element_by_xpath(address_1).send_keys("Test 1")

print("11: Sending address second line")
driver.find_element_by_xpath(address_2).send_keys("Test 2")

print("12: Sending city")
driver.find_element_by_xpath(city).send_keys("Test city")

print("13: Choosing state from list")
driver.find_element_by_xpath(state).click()

print("14: Sending zip code")
driver.find_element_by_xpath(zip_code).send_keys("00000")

print("15: Choosing country from list")
driver.find_element_by_xpath(country).click()

print("16: Sending mobile phone number")
driver.find_element_by_xpath(mobile_phone).send_keys("123123123")

print("17: Saving address")
driver.find_element_by_xpath(address_save).click()

print("18: Deleting added address from address book")
driver.find_element_by_xpath(address_delete).click()
driver.switch_to.alert.accept()

print("19: Checking if address was successfully deleted")
address_removed = driver.find_element_by_xpath(no_addresses)
if address_removed.is_displayed():
    print("19a: Address was removed")
else:
    print("ERROR - Address not removed properly")

print("20: Logging out")
driver.find_element_by_xpath(logout_btn).click()

print("21: Checking correct log-out")
if driver.current_url == account_page:
    print ("Logout was successful")
    driver.close()
else:
    print("Error occured - not logged out")

end_time = time.time()
print("Total execution time: {:0.2f} seconds".format(end_time - start_time))