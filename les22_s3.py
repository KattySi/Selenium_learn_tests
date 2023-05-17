from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

try:
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("Ivan@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'add_to_les22_s3.txt')
    element = browser.find_element(By.ID, "file")
    element.send_keys(file_path)

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
