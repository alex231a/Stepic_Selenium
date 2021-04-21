from selenium import webdriver
import time
import os

link = 'http://suninjuly.github.io/file_input.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_element_by_name('firstname')
    first_name.send_keys('Alexander')
    last_name = browser.find_element_by_name('lastname')
    last_name.send_keys('King')
    email = browser.find_element_by_name('email')
    email.send_keys('123@gmail.com')

    path = os.getcwd()
    file_path = os.path.join(path, 'file.txt')
    print(file_path)

    file = browser.find_element_by_name('file')
    file.send_keys(file_path)

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(10)
    browser.quit()
