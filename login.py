from selenium import webdriver
import time

driver = webdriver.Chrome()

website = "http://automationpractice.com/index.php"
login_btn = '//*[@id="header"]/div[2]/div/div/nav/div[1]/a'
login_mail = '//*[@id="email"]'
login_pwd = '//*[@id="passwd"]'
login_submit = '//*[@id="SubmitLogin"]'

start_time = time.time()

print("TEST: Login \nStart: Go to test website")
driver.get(website)

print("1: Click login button")
driver.find_element_by_xpath(login_btn).click()

print("2: Fill login form with email and password")
driver.find_element_by_xpath(login_mail).send_keys("emailer5k+selenium@gmail.com")
driver.find_element_by_xpath(login_pwd).send_keys("12345")

print("3: Click submit button")
driver.find_element_by_xpath(login_submit).click()

print("4: Checking for current URL")
if driver.current_url != website:
    driver.close()
    print("FINISHED: Test was successful")
else:
    print("Error occured")

end_time = time.time()
print("Total execution time: {:0.2f} seconds".format(end_time - start_time))