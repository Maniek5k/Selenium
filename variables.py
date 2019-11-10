import random
import time
from termcolor import colored

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.set_page_load_timeout(30)

website = "http://automationpractice.com/index.php"

## Login

login_email = "emailer5k+selenium@gmail.com"
login_password = "12345"

login_btn = '//*[@id="header"]/div[2]/div/div/nav/div[1]/a'
login_mail = '//*[@id="email"]'
login_pwd = '//*[@id="passwd"]'
login_submit = '//*[@id="SubmitLogin"]'
logout_btn = '//*[@id="header"]/div[2]/div/div/nav/div[2]/a'
login_page = 'http://automationpractice.com/index.php?controller=authentication&back=my-account'
account_page = 'http://automationpractice.com/index.php?controller=my-account'

## Subscribe to newsletter

prefix_create = random.randint(0, 9999)
newsletter_mail = str(prefix_create) + '@testmail.com'

newsletter_input = '#newsletter-input'
newsletter_submit = '//*[@id="newsletter_block_left"]/div/form/div/button'
newsletter_resubmit = '//*[@id="newsletter_block_left"]/div/form/div/button'


newsletter_success = 'alert-success'
newsletter_failed = 'alert-danger'

success_message = "Newsletter : You have successfully subscribed to this newsletter."
failed_message = "Newsletter : This email address is already registered."

## Add product to wishlist

wishlist_login = "emailer5k+wishlist@gmail.com"
wishlist_password = "12345"

wishlist_product = "http://automationpractice.com/index.php?id_product=2&controller=product"
wishlist_my_acc = "http://automationpractice.com/index.php?fc=module&module=blockwishlist&controller=mywishlist"

wishlist_prod_name = '//*[@id="center_column"]/div/div/div[3]/h1'
wishlist_add = '//*[@id="wishlist_button"]'

wishlist_open = '/html/body/div/div[2]/div/div[3]/div[2]/div/div[1]/table/tbody/tr/td[1]/a'
wishlist_added_click = '//*[@id="wlp_2_7"]/div/div[1]/div/a/img'

wishlist_remove = '/html/body/div/div[2]/div/div[3]/div[2]/div/div[1]/table/tbody/tr/td[6]/a/i'

## Create account

new_account_email = str(prefix_create) + '@testmail.com'

create_acc_mail = '//*[@id="email_create"]'
create_acc_submit = '//*[@id="SubmitCreate"]'

new_acc_radio = '//*[@id="id_gender1"]'
new_acc_first_name = '//*[@id="customer_firstname"]'
new_acc_last_name = '//*[@id="customer_lastname"]'
new_acc_password = '//*[@id="passwd"]'
new_acc_register = '//*[@id="submitAccount"]'

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

## Add to basket test

basket_email = 'emailer5k+addtobasket@gmail.com'
basket_password = '12345'

basket_product_page = "http://automationpractice.com/index.php?id_product=3&controller=product"

basket_name = '//*[@id="center_column"]/div/div/div[3]/h1'
basket_added_product_name = '/html/body/div/div[2]/div/div[3]/div/div[2]/table/tbody/tr/td[2]/p/a'

basket_add = '//*[@id="add_to_cart"]/button'
basket_remove = '/html/body/div/div[2]/div/div[3]/div/div[2]/table/tbody/tr/td[7]/div/a'

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
pay_by_check = '//*[@id="HOOK_PAYMENT"]/div[2]/div/p/a'
place_order = '//*[@id="cart_navigation"]/button'
order_confirmation = '//*[@id="center_column"]/p/a'
order_history = "http://automationpractice.com/index.php?controller=history"
