# alert = browser.switch_to.alert
# alert.accept()
#
# alert = browser.switch_to.alert
# alert_text = alert.text
#
# confirm = browser.switch_to.alert
# confirm.accept()
# confirm.dismiss()
#
# prompt = browser.switch_to.alert
# prompt.send_keys("My answer")
# prompt.accept()

from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/alert_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    val = browser.find_element_by_id('input_value')
    x = val.text
    rez = calc(x)
    field = browser.find_element_by_id('answer')
    field.send_keys(rez)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
