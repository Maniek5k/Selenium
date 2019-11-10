from variables import *

start_time = time.time()

print("TEST STARTED: Subscribe to newsletter \nStart: Go to test website")
driver.get(website)

print("1: Sending new email to newsletter subscribe")
driver.find_element_by_css_selector(newsletter_input).send_keys(newsletter_mail)

print("2: Submitting subscription")
driver.find_element_by_xpath(newsletter_submit).click()

print("3: Checking if subscribed successfully")
if driver.find_element_by_class_name(newsletter_success).text == success_message:
    print("Displayed message: " + driver.find_element_by_class_name(newsletter_success).text)
else:
    print("Error occured - already registered")

print("4: Providing the same e-mail address once again - checking for correct alert message")
driver.find_element_by_css_selector(newsletter_input).send_keys(newsletter_mail)
driver.find_element_by_css_selector(newsletter_input).send_keys(Keys.RETURN)

if driver.find_element_by_class_name(newsletter_failed).text == failed_message:
    print("Displayed message: " + driver.find_element_by_class_name(newsletter_failed).text)
else:
    print("Error occured - different message than expected")

driver.close()
print("TEST FINISHED SUCCESSFULLY")

end_time = time.time()
print("Total execution time: {:0.2f} seconds".format(end_time - start_time))