# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.get("https://exoticsad.com")
# button = browser.find_element_by_id("logo")
#
#
# browser.close()
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "https://exoticsad.com"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, "#cart a")
    button.click()
    time.sleep(10)
# закрываем браузер после всех манипуляций
finally:
    browser.quit()
