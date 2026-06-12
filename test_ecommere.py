from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_search():

    driver = webdriver.Chrome()

    driver.get("SITE_URL")

    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "input"))
    )

    search = driver.find_element(By.TAG_NAME, "input")

    search.send_keys("product_name")
    search.send_keys(Keys.RETURN)

    WebDriverWait(driver, 10).until(
        lambda d: "product_name" in d.page_source.lower()
    )

    print("Title:", driver.title)
    print("URL:", driver.current_url)

    assert "product_name" in driver.page_source.lower()

    driver.quit()