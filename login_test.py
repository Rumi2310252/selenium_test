from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com")

    # Wait until username input is present
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))

    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")

    # Wait until submit button clickable
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

    # Wait until dashboard url appears
    WebDriverWait(driver, 10).until(lambda d: "dashboard" in d.current_url.lower())
    assert "dashboard" in driver.current_url.lower()

    driver.quit()