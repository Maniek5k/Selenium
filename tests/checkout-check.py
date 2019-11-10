from variables import *

start_time = time.time()

print(colored("TEST STARTED: Checkout - pay by check\nStart: Go to test website", "green", attrs=['bold']))
driver.get(website)

print("1: Clicking add to cart CTA")
driver.find_element_by_xpath(add_to_cart).click()

print("2: Going to login page")
driver.find_element_by_xpath(go_to_login).click()

print("3: Providing login credentials and submitting form")
driver.find_element_by_xpath(email).send_keys(login_email)
driver.find_element_by_xpath(password).send_keys(login_password)
driver.find_element_by_xpath(submit).click()

print("4: Going to basket - checkout")
driver.find_element_by_xpath(go_to_checkout).click()

print("5: Proceeding through checkout")
driver.find_element_by_xpath(proceed).click()
driver.find_element_by_xpath(proceed_2).click()

print("6: Ticking necessary checkbox on checkout screen")
driver.find_element_by_xpath(checkout_checkbox).click()

print("7: Proceeding to payment")
driver.find_element_by_xpath(go_to_payment).click()

print("8: Choosing Pay By Wire option")
driver.find_element_by_xpath(pay_by_check).click()

print("9: Placing order")
driver.find_element_by_xpath(place_order).click()

print("10: Order confirmation page - going back to order history")
driver.find_element_by_xpath(order_confirmation).click()
if driver.current_url == order_history:
    print(colored("Order placed successfully", "blue"))

    print("11: Logging out")
    driver.find_element_by_xpath(logout_btn).click()

    print(colored("TEST FINISHED SUCCESSFULLY", "green", attrs=['bold']))
    driver.close()
else:
    print("Error occured")

end_time = time.time()
print(colored("Total execution time: {:0.2f} seconds".format(end_time - start_time), "cyan"))