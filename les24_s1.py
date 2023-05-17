from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
# browser.implicitly_wait(5)
browser.get("http://suninjuly.github.io/explicit_wait2.html")
try:
    button = browser.find_element(By.ID, "book")
    price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, 'price'), "$100"))
    button.click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    button_two = browser.find_element(By.ID, "solve").click()


finally:
    time.sleep(10)
    browser.quit()

# print(__name__)
