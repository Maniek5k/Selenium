from test_data import *

start_time = time.time()

print(colored("TEST STARTED: Search \nStart: Go to test website", "green", attrs=['bold']))
driver.get(website)

print("1: Sending string to search for "+search_term)
driver.find_element_by_xpath(search_input).send_keys(search_term)

print("2: Submitting search")
driver.find_element_by_xpath(search_submit).click()

print("CHECK: Checking for correct product displayed")
result_product = driver.find_element_by_xpath(search_result_name).text

if result_product == search_term:
    print(colored("SUCCESS: Search for products works correctly", "blue"))
else:
    print("Error occurred")

print("3: Another search attempt - searching for "+search_404)
driver.find_element_by_xpath(search_input).clear()
driver.find_element_by_xpath(search_input).send_keys(search_404)

print("4: Submitting search")
driver.find_element_by_xpath(search_submit).click()

print("CHECK: Checking for correct alert displayed - no products match search query")
result_failed = driver.find_element_by_xpath(search_failed_alert).text

if result_failed == search_failed_alert_text:
    print(colored("SUCCESS: Search alert works correctly", "blue"))
    driver.close()
    print(colored("TEST FINISHED SUCCESSFULLY", "green", attrs=['bold']))
else:
    print("Error occurred")

end_time = time.time()
print(colored("Total execution time: {:0.2f} seconds".format(end_time - start_time), "cyan"))
