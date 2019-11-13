from variables import *

start_time = time.time()

print(colored("TEST STARTED: Adding product to wishlist \nStart: Go to test website", "green", attrs=['bold']))
driver.get(website)

print("1: Click login button")
driver.find_element_by_xpath(login_btn).click()

print("2: Fill login form with email and password")
driver.find_element_by_xpath(login_mail).send_keys(wishlist_login)
driver.find_element_by_xpath(login_pwd).send_keys(wishlist_password)

print("3: Click submit button")
driver.find_element_by_xpath(login_submit).click()

print("4: Checking for current URL")
if driver.current_url == account_page:
    print(colored("Login was successful", "blue"))
else:
    print(colored("Error occurred", "red"))

print("5: Go to product page")
driver.get(wishlist_product)

wishlist_name = driver.find_element_by_xpath(wishlist_prod_name).text
print("6: Product that will be added to wishlist: "+wishlist_name+colored("\nAdding to wishlist", "blue"))

driver.find_element_by_xpath(wishlist_add).click()

print("7: Going to wishlist section on my account")
driver.get(wishlist_my_acc)

print("8: Opening wishlist")
driver.implicitly_wait(2)
driver.find_element_by_xpath(wishlist_open).click()

print("9: Checking for correct product added to wishlist - clicking product image")
driver.find_element_by_xpath(wishlist_added_click).click()

wishlist_added = driver.find_element_by_xpath(wishlist_prod_name).text

if wishlist_name == wishlist_added:
    print(colored("Product " + wishlist_name + " was correctly added to wishlist", "blue"))
else:
    print("error")

print("10: Going back to wishlist section")
driver.get(wishlist_my_acc)

print("11: Removing wishlist from my account")
driver.find_element_by_xpath(wishlist_remove).click()
driver.implicitly_wait(1)
driver.switch_to.alert.accept()

print(colored("TEST FINISHED SUCCESSFULLY", "green", attrs=['bold']))
driver.close()

end_time = time.time()
print(colored("Total execution time: {:0.2f} seconds".format(end_time - start_time), "cyan"))