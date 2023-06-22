import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, WebDriverException

chrome_driver_path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome()

url = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(url)

def check():
    store = driver.find_element(By.CSS_SELECTOR, "div#store").find_elements(By.CSS_SELECTOR, "div")[::-1]
    
    for element in store[1:]:
        try:
            rate_element = elements.find_element(By.CSS_SELECTOR, "b")
            rate = rate_element.text.split("-")[1].strip().replace(",", "")
            money = driver.find_element(By.CSS_SELECTOR, "div#money").text.strip().replace(",", "")
            
            if int(rate) < int(money):
                rate_element.click()  # Click to purchase if rate is lower than money
        except (NoSuchElementException, StaleElementReferenceException, WebDriverException):
            pass

timeout = time.time() + 10

while True:
    if time.time() > timeout:
        check()  # Perform the check for purchasing upgrades
        print("timeout")
        timeout = time.time() + 10
    
    driver.find_element(By.CSS_SELECTOR, "div#cookie").click()  # Click on the cookie
