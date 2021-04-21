# from selenium import webdriver
# import time
#
# link = "https://exoticsad.com"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     text = browser.find_element_by_link_text('КАРТА')
#     if text:
#         print(text)
#     else:
#         print('Error')
#
# finally:
#     time.sleep(3)
#     browser.quit()


from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/find_link_text"
text = str(math.ceil(math.pow(math.pi, math.e)*10000))
print(text)
try:
    browser = webdriver.Chrome()
    browser.get(link)
    text_find = browser.find_element_by_link_text(text)
    text_find.click()

    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys("Alex")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Yakovenko")
    input3 = browser.find_element_by_class_name('city')
    input3.send_keys("Kyiv")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Ukraine")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(3)
    browser.quit()
