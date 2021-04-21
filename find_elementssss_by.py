# from selenium import webdriver
# import time
#
# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/huge_form.html")
#     elements = browser.find_elements_by_tag_name('input')
#     for element in elements:
#         element.send_keys("Мой ответ")
#
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#     alert = browser.switch_to_alert()
#     print(alert.text)
# finally:
#     time.sleep(30)
#     browser.quit()


# from selenium import webdriver
# import time
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(" http://suninjuly.github.io/find_xpath_form")
#     elements = browser.find_elements_by_tag_name('input')
#     for element in elements:
#         element.send_keys("Мой ответ")
#
#     button = browser.find_element_by_xpath('/html/body/div/form/div[6]/button[3]')
#     button.click()
#     alert = browser.switch_to_alert()
#     print(alert.text)
# finally:
#     time.sleep(10)
#     browser.quit()


from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    element1 = browser.find_element_by_css_selector("input.form-control.first")
    element1.send_keys("Мой ответ")

    element2 = browser.find_element_by_css_selector("input.form-control.second")
    element2.send_keys("Мой ответ")

    element2 = browser.find_element_by_css_selector("input.form-control.third")
    element2.send_keys("Мой ответ")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(10)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()
