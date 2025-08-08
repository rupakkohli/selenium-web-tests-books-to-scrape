# tests/test_pagination.py
# Goal: check if "next" button works in a category with multiple pages.

from selenium.webdriver.common.by import By
import time  # for a basic pause while learning; will replace later

def test_science_category_pagination(driver):
    driver.get("https://books.toscrape.com/")
    driver.find_element(By.LINK_TEXT, "Science").click()

    # Check if "next" button exists
    next_buttons = driver.find_elements(By.CSS_SELECTOR, "ul.pager li.next a")
    if not next_buttons:
        assert False, "No pagination found for Science category"

    # Click the next button
    next_buttons[0].click()
    time.sleep(1)  # TODO: replace with proper wait

    # Check the URL changed to page-2
    assert "page-2.html" in driver.current_url
