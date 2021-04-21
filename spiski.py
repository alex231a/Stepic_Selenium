from selenium import webdriver
import math
import time
from selenium.webdriver.support.ui import Select


link = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    val1a = browser.find_element_by_id('num1')
    val1 = val1a.text
    val2a = browser.find_element_by_id('num2')
    val2 = val2a.text
    rez = int(val1) + int(val2)
    print(rez)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(rez))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
