from test_data import *

start_time = time.time()

print(colored("TEST STARTED: Pay by check\nStart: Go to test website", "green", attrs=['bold']))
driver.get(website)

print("1: Going to login page")
driver.find_element_by_xpath(go_to_login).click()

print("2: Providing login credentials and submitting form")
driver.find_element_by_xpath(email).send_keys(login_email)
driver.find_element_by_xpath(password).send_keys(default_password)
driver.find_element_by_xpath(submit).click()

print("3: Going to product page")
driver.get(wishlist_product)
product_sku = driver.find_element_by_xpath(product_page_sku).text

print("4: Clicking add to cart CTA")
driver.find_element_by_xpath(add_to_cart).click()

print("5: Going to basket - checkout")
driver.find_element_by_xpath(go_to_checkout).click()

print("6: Proceeding through checkout")
driver.find_element_by_xpath(proceed).click()
driver.find_element_by_xpath(proceed_2).click()

print("7: Ticking necessary checkbox on checkout screen")
driver.find_element_by_xpath(checkout_checkbox).click()

print("8: Proceeding to payment")
driver.find_element_by_xpath(go_to_payment).click()

print("9: Choosing Pay By Wire option")
driver.find_element_by_xpath(pay_by_wire).click()

print("10: Placing order")
driver.find_element_by_xpath(place_order).click()

print("11: Order confirmation page - going back to order history")
driver.find_element_by_xpath(order_confirmation).click()

driver.implicitly_wait(5)
print("12: Unfolding last order on order list")
driver.find_element_by_xpath(order_unfold).click()
driver.implicitly_wait(5)
html = driver.find_element_by_tag_name('html')
html.send_keys(Keys.END)

print("CHECK: Checking if ordered product SKU matched SKU on product page")
order_sku = driver.find_element_by_xpath(ordered_sku).text

if order_sku == product_sku:
    print(colored("SUCCESS: Order placed successfully", "blue"))
    print("11: Logging out")
    driver.find_element_by_xpath(logout_btn).click()
else:
    print("Error occured")

print("13: Checking correct log-out")
if driver.current_url == order_logout_page:
    print(colored("SUCCESS: Logout was successful", "blue"))
    driver.close()
    print(colored("TEST FINISHED SUCCESSFULLY", "green", attrs=['bold']))
else:
    print("Error occurred")

end_time = time.time()
print(colored("Total execution time: {:0.2f} seconds".format(end_time - start_time), "cyan"))
