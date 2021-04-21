# browser.switch_to.window(window_name)
# new_window = browser.window_handles[1]
# first_window = browser.window_handles[0]

from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/redirect_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    print(browser.window_handles)
    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]
    browser.switch_to.window(new_window)
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
