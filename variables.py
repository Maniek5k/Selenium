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

## Generate random string for names etc.

import random
import string

def randomString(stringLength):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))


## Pages

default_password = "12345"

website = "http://automationpractice.com/index.php"
login_page = 'http://automationpractice.com/index.php?controller=authentication&back=my-account'
change_password_logout_page = "http://automationpractice.com/index.php?controller=authentication&back=identity"
account_page = 'http://automationpractice.com/index.php?controller=my-account'
address_page = 'http://automationpractice.com/index.php?controller=addresses'
wishlist_product = "http://automationpractice.com/index.php?id_product=2&controller=product"
wishlist_my_acc = "http://automationpractice.com/index.php?fc=module&module=blockwishlist&controller=mywishlist"
order_history = "http://automationpractice.com/index.php?controller=history"
basket_product_page = "http://automationpractice.com/index.php?id_product=3&controller=product"

## Login

login_email = "emailer5k+selenium@gmail.com"

login_btn = '//*[@id="header"]/div[2]/div/div/nav/div[1]/a'
login_mail = '//*[@id="email"]'
login_pwd = '//*[@id="passwd"]'
login_submit = '//*[@id="SubmitLogin"]'
logout_btn = '//*[@id="header"]/div[2]/div/div/nav/div[2]/a'

## Recover password

recover_password = '//*[@id="login_form"]/div/p[1]/a'
recover_email = '//*[@id="email"]'
recover_confirm = '//*[@id="form_forgotpassword"]/fieldset/p/button'

recover_success = '//*[@id="center_column"]/div/p'
recover_success_text = "A confirmation email has been sent to your address: emailer5k+selenium@gmail.com"

## Change password
prefix_create = random.randint(0, 9999)

change_password_email = "emailer5k+pwdchange@gmail.com"
new_password = str(prefix_create)

change_password_info = 'icon-user'
change_password_current = '//*[@id="old_passwd"]'
change_password_new = '//*[@id="passwd"]'
change_password_confirm = '//*[@id="confirmation"]'
change_password_save = 'submitIdentity'
change_password_alert = '//*[@id="center_column"]/div/p'
change_password_success_text = 'Your personal information has been successfully updated.'

## Change personal informations

change_info_email = "emailer5k+personalchange@gmail.com"

change_info_name = '//*[@id="firstname"]'
change_info_lastname = '//*[@id="lastname"]'

test_name = randomString(6)
test_lastname = randomString(7)

## Contact us form

contact_test_email = "contact@testmail.com"
contact_test_message = "This is test contact message."

contact_us_btn = '//*[@id="contact-link"]/a'
contact_subject = '//*[@id="id_contact"]/option[text()="Webmaster"]'
contact_email = '//*[@id="email"]'
contact_message = '//*[@id="message"]'
contact_submit = '//*[@id="submitMessage"]'
contact_success = '//*[@id="center_column"]/p'
contact_success_text = "Your message has been successfully sent to our team."


## Subscribe to newsletter

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
