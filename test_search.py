from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_google_search():

    driver = webdriver.Chrome()

    driver.get("https://www.google.com")

    search_box = driver.find_element(By.NAME, "q")

    search_box.send_keys("Python")
    search_box.send_keys(Keys.RETURN)

    time.sleep(3)

    print("Title:", driver.title)
    print("URL:", driver.current_url)

    assert "Python" in driver.title

    driver.quit()