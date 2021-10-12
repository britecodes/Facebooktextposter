from selenium import webdriver
from time import sleep
import pyautogui

# Note this script requires selenium webdriver installed for firefox/ chrome but you will have to look that up yourself
# because i am lazy lol
# Script written by Britecodes

username = " "  # insert your phone number/ email
password = " "  # insert your password
post_message = " "  # insert the message you wish to post

driver = webdriver.Firefox()  # change the 'Firefox' to chrome if you wish to use this with chrome webdriver instead
driver.get("https://www.facebook.com")
driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('pass').send_keys(password)
driver.find_element_by_name('login').click()
sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div['
                             '2]/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/div').click()
sleep(2)
pyautogui.typewrite(post_message)
sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div['
                             '2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/div/div').click()

print("Script complete!")