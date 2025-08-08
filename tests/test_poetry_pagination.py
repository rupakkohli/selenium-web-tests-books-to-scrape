from selenium.webdriver.common.by import By
import time

def test_poetry_category_pagination(driver):
    driver.get("https://books.toscrape.com/")
    driver.find_element(By.LINK_TEXT, "Poetry").click()

    # Check if "next" button exists
    next_buttons = driver.find_elements(By.CSS_SELECTOR, "ul.pager li.next a")
    assert next_buttons, "Expected pagination for Poetry category"

    # Click next
    next_buttons[0].click()
    time.sleep(1)  # TODO: replace with WebDriverWait

    # Confirm URL updated
    assert "page-2.html" in driver.current_url
