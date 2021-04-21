# from selenium import webdriver
# browser = webdriver.Chrome()
# #browser.execute_script("alert('Robots at work');")
# #browser.execute_script("document.title='Script executing';")
# browser.execute_script("document.title='Script executing';alert('Robots at work');")

# from selenium import webdriver
#
# browser = webdriver.Chrome()
# link = "https://SunInJuly.github.io/execute_script.html"
# browser.get(link)
# button = browser.find_element_by_tag_name("button")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# button.click()


from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/execute_script.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    el = browser.find_element_by_id('input_value')
    val = el.text
    print(val)
    rez = calc(int(val))
    field = browser.find_element_by_id('answer')
    field.send_keys(rez)
    check_box_robot = browser.find_element_by_id('robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);", check_box_robot)
    check_box_robot.click()
    rbt = browser.find_element_by_css_selector('[for="robotsRule"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", rbt)
    rbt.click()
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    time.sleep(10)
    browser.quit()

