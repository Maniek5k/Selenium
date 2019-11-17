from test_data import *

start_time = time.time()

print(colored("TEST STARTED: Add to basket\nStart: Go to test website", "green", attrs=['bold']))
driver.get(website)

print("1: Go to login page")
driver.find_element_by_xpath(go_to_login).click()

print("2: Providing login credentials and submitting form")
driver.find_element_by_xpath(email).send_keys(login_email)
driver.find_element_by_xpath(password).send_keys(default_password)
driver.find_element_by_xpath(submit).click()

print("3: Checking for current URL")
if driver.current_url == account_page:
    print(colored("Login was successful", "blue"))
else:
    print("Error occurred")

print("4: Going to product page")
driver.get(basket_product_page)
product_name = driver.find_element_by_xpath(basket_name).text

print("5: Adding product to basket")
driver.find_element_by_xpath(basket_add).click()

print("6: Going to basket")
driver.find_element_by_xpath(go_to_checkout).click()
added_product_name = driver.find_element_by_xpath(basket_added_product_name).text

print("7: Validating that correct product is in basket")
if product_name == added_product_name:
    print(colored("Correct product in basket", "blue"))
else:
    print("Error occurred")

print("8: Going to account page")
driver.get(account_page)

print("9: Logging out")
driver.find_element_by_xpath(logout_btn).click()

print("10: Checking correct log-out")
if driver.current_url == login_page:
    print(colored("SUCCESS: Logout was successful", "blue"))
    driver.close()
    print(colored("TEST FINISHED SUCCESSFULLY", "green", attrs=['bold']))
else:
    print("Error occurred")

end_time = time.time()
print(colored("Total execution time: {:0.2f} seconds".format(end_time - start_time), "cyan"))