# from selenium import webdriver
# import time
#
# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/wait1.html")
#
# time.sleep(3)
#
# button = browser.find_element_by_id("verify")
# button.click()
# message = browser.find_element_by_id("verify_message")
#
# assert "successful" in message.text

# #2
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# # говорим WebDriver искать каждый элемент в течение 5 секунд
# browser.implicitly_wait(5)
#
# browser.get("http://suninjuly.github.io/wait1.html")
#
# button = browser.find_element_by_id("verify")
# button.click()
# message = browser.find_element_by_id("verify_message")
#
# assert "successful" in message.text

# #3
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# # говорим WebDriver ждать все элементы в течение 5 секунд
# browser.implicitly_wait(10)
#
# browser.get("http://suninjuly.github.io/wait2.html")
#
# button = browser.find_element_by_id("verify")
# button.click()
# message = browser.find_element_by_id("verify_message")
#
# assert "successful" in message.text

# #4
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
#
# browser = webdriver.Chrome()
#
# browser.get("http://suninjuly.github.io/wait2.html")
#
# # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
# button = WebDriverWait(browser, 5).until(
#     EC.element_to_be_clickable((By.ID, "verify"))
# )
# button.click()
# message = browser.find_element_by_id("verify_message")
#
# assert "successful" in message.text


# # говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
# button = WebDriverWait(browser, 5).until_not(
#     EC.element_to_be_clickable((By.ID, "verify"))
# )

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    wait = WebDriverWait(browser, 12)
    element = wait.until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    if element:
        print(element)
        button = browser.find_element_by_id('book')
        button.click()

    val = browser.find_element_by_id('input_value')
    x = val.text
    rez = calc(x)
    field = browser.find_element_by_id('answer')
    field.send_keys(rez)
    button = browser.find_element_by_id("solve")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
