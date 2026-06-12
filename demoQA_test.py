from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_form():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get("https://demoqa.com/text-box")

        driver.find_element(By.ID, "userName").send_keys("Jayna")
        driver.find_element(By.ID, "userEmail").send_keys("test@gmail.com")
        driver.find_element(By.ID, "currentAddress").send_keys("Dhaka")
        driver.find_element(By.ID, "permanentAddress").send_keys("Bangladesh")

        submit_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "submit"))
        )

        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_button)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "submit"))
        )

        submit_button.click()

    finally:
        driver.quit()