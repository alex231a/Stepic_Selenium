from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/get_attribute.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    element = browser.find_element_by_id('treasure')
    attr = element.get_attribute('valuex')
    print(attr)
    result = calc(int(attr))
    print(result)

    field = browser.find_element_by_id('answer')
    field.send_keys(result)

    robot_ch_b = browser.find_element_by_id('robotCheckbox')
    robot_ch_b.click()

    robot_rule_btn = browser.find_element_by_id('robotsRule')
    robot_rule_btn.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
