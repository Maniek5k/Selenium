from selenium import webdriver
import time

## Variables, selectors

driver = webdriver.Chrome()
website = "http://automationpractice.com/index.php"
addToCart = '//*[@id="homefeatured"]/li[1]/div/div[2]/div[2]/a[1]'
goToLogin = '//*[@id="header"]/div[2]/div/div/nav/div[1]/a'
goToCheckout = '//*[@id="header"]/div[3]/div/div/div[3]/div/a'
email = '//*[@id="email"]'
password = '//*[@id="passwd"]'
submit = '//*[@id="SubmitLogin"]'
proceed = '//*[@id="center_column"]/p[2]/a[1]'
proceed2 = '//*[@id="center_column"]/form/p/button'
checkoutCheckbox = '//*[@id="cgv"]'
goToPayment = '//*[@id="form"]/p/button'
payByWire = '//*[@id="HOOK_PAYMENT"]/div[1]/div/p/a'
confirmOrder = '//*[@id="cart_navigation"]/button'

## Tests

start_time = time.time()

print("STARTED\n0: Going to test website")
driver.get(website)
print("1: Clicking add to cart CTA")
driver.find_element_by_xpath(addToCart).click()
print("2: Going to login page")
driver.find_element_by_xpath(goToLogin).click()
print("3: Providing login credentials and submitting form")
driver.find_element_by_xpath(email).send_keys("emailer5k+selenium@gmail.com")
driver.find_element_by_xpath(password).send_keys("12345")
driver.find_element_by_xpath(submit).click()
print("4: Going to basket - checkout")
driver.find_element_by_xpath(goToCheckout).click()
print("5: Proceeding through checkout")
driver.find_element_by_xpath(proceed).click()
driver.find_element_by_xpath(proceed2).click()
print("6: Ticking necessary checkbox on checkout screen")
driver.find_element_by_xpath(checkoutCheckbox).click()
print("7: Proceeding to payment")
driver.find_element_by_xpath(goToPayment).click()
print("8: Choosing Pay By Wire option")
driver.find_element_by_xpath(payByWire).click()
print("9: Placing order")
driver.find_element_by_xpath(confirmOrder).click()
print("10: Closing Chrome")
driver.close()
end_time = time.time()
print("FINISHED\nTotal execution time: {:0.2f} seconds".format(end_time - start_time))