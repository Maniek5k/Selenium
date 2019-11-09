from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

website = "http://automationpractice.com/index.php"

## Login test

login_email = "emailer5k+selenium@gmail.com"
login_password = "12345"

login_btn = '//*[@id="header"]/div[2]/div/div/nav/div[1]/a'
login_mail = '//*[@id="email"]'
login_pwd = '//*[@id="passwd"]'
login_submit = '//*[@id="SubmitLogin"]'
logout_btn = '//*[@id="header"]/div[2]/div/div/nav/div[2]/a'
login_page = 'http://automationpractice.com/index.php?controller=authentication&back=my-account'
account_page = 'http://automationpractice.com/index.php?controller=my-account'

## Add new address

address_email = "emailer5k+addnewaddress@gmail.com"
address_pwd = "12345"

address_page = 'http://automationpractice.com/index.php?controller=addresses'
add_new_address = '//*[@id="center_column"]/div/a'
first_name = '//*[@id="firstname"]'
last_name = '//*[@id="lastname"]'
company = '//*[@id="company"]'
address_1 = '//*[@id="address1"]'
address_2 = '//*[@id="address2"]'
city = '//*[@id="city"]'
state = "//*[@id='id_state']/option[text()='Alaska']"
zip_code = '//*[@id="postcode"]'
country = "//*[@id='id_country']/option[text()='United States']"
mobile_phone = '//*[@id="phone_mobile"]'
address_reference = '//*[@id="alias"]'
address_save = '//*[@id="submitAddress"]'
address_delete = '//*[@id="center_column"]/div[1]/div/div/ul/li[9]/a[2]'
address_block = '//*[@id="center_column"]/div[1]/div/div/ul/li[1]/h3'
no_addresses = '//*[@id="center_column"]/p[2]'


## Checkout test

add_to_cart = '//*[@id="homefeatured"]/li[1]/div/div[2]/div[2]/a[1]'
go_to_login = '//*[@id="header"]/div[2]/div/div/nav/div[1]/a'
go_to_checkout = '//*[@id="header"]/div[3]/div/div/div[3]/div/a'
email = '//*[@id="email"]'
password = '//*[@id="passwd"]'
submit = '//*[@id="SubmitLogin"]'
proceed = '//*[@id="center_column"]/p[2]/a[1]'
proceed_2 = '//*[@id="center_column"]/form/p/button'
checkout_checkbox = '//*[@id="cgv"]'
go_to_payment = '//*[@id="form"]/p/button'
pay_by_wire = '//*[@id="HOOK_PAYMENT"]/div[1]/div/p/a'
place_order = '//*[@id="cart_navigation"]/button'
order_confirmation = '//*[@id="center_column"]/p/a'
order_history = "http://automationpractice.com/index.php?controller=history"