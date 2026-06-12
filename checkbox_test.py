from selenium import webdriver
from selenium.webdriver.common.by import By

def test_checkbox():

    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    boxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

    boxes[0].click()

    assert boxes[0].is_selected()

    driver.quit()