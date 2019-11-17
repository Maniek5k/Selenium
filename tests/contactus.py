from test_data import *

start_time = time.time()

print(colored("TEST STARTED: Contact Us form \nStart: Go to test website", "green", attrs=['bold']))
driver.get(website)

print("1: Going to contact us form page")
driver.find_element_by_xpath(contact_us_btn).click()

print("2: Sending customer e-mail address")
driver.find_element_by_xpath(contact_email).send_keys(contact_test_email)

print("3: Choosing contact subject - Webmaster")
driver.find_element_by_xpath(contact_subject).click()

print("4: Sending contact test message into textarea")
driver.find_element_by_xpath(contact_message).send_keys(contact_test_message)

print("5: Submitting contact form")
driver.find_element_by_xpath(contact_submit).click()

print("CHECK: Checking for correct success message")
contact_alert_success = driver.find_element_by_xpath(contact_success).text

if contact_alert_success == contact_success_text:
    print(colored("SUCCESS: Contact email was correctly sent", "blue"))
    driver.close()
    print(colored("TEST FINISHED SUCCESSFULLY", "green", attrs=['bold']))
else:
    print("Error occurred")

end_time = time.time()
print(colored("Total execution time: {:0.2f} seconds".format(end_time - start_time), "cyan"))
