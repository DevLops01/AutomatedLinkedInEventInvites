from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# Get User Input Fields
get_username = input('Please enter your LinkedIn Username or Email. \n')
get_password = input('Please enter your LinkedIn Password.\n')
get_event_name = input('Please select the event name you would like to auto invite contacts to. (* CASE SENSITIVE *)\n')
get_location = input('Please enter the Location of the connections you would like to invite. (Full State required., '
                     'i.e Houston, Texas) press enter to skip.\n')
# get_industry = input('Please select the industry of the connections you would like to invite.\n')

print("Starting new chrome session...")
time.sleep(1)

# Open webdriver browser
browser = webdriver.Chrome(r"C:\Users\Paul\Desktop\chromedriver") # Enter the location of your chromedriver here
browser.get(r"https://linkedin.com")

# Sign in on the browser
signIn = browser.find_element_by_link_text('Sign in')
signIn.click()

username = browser.find_element_by_id('username')
password = browser.find_element_by_id('password')
username.send_keys(get_username)
password.send_keys(get_password)

click_login = browser.find_element_by_class_name('btn__primary--large')
click_login.click()

# Select event name
event_name = browser.find_element_by_link_text(get_event_name)
event_name.click()
time.sleep(2)

# click invite connections button
invite_connections = browser.find_element_by_class_name('artdeco-button--primary')
invite_connections.click()


# Sets location filters
def filter_location():
    # click the location button
    set_location = browser.find_element_by_class_name('artdeco-button--1')
    set_location.click()

    # Enter location
    type_location = browser.find_element_by_class_name('ember-text-field')
    type_location.send_keys(get_location + ' Area')
    time.sleep(1)

    # Select exact location from drop down menu
    type_location.send_keys(Keys.ENTER)

    # click apply button for location
    apply_location = browser.find_element_by_class_name('facet-collection-list__apply-button')
    apply_location.click()


# Set location if specified
if get_location != '':
    filter_location()

check_invitee = browser.find_element_by_class_name('invitee-picker-connections-result-item__checkbox')
check_invitee.click()



