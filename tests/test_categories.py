# tests/test_categories.py
# Goal: click a category and sanity-check the basics.
# TODO: later try another category and compare counts.

from selenium.webdriver.common.by import By

def test_travel_category_basics(driver):
    driver.get("https://books.toscrape.com/")

    # Click the "Travel" link in the left sidebar
    driver.find_element(By.LINK_TEXT, "Travel").click()

    # Heading should be "Travel"
    heading = driver.find_element(By.CSS_SELECTOR, "div.page-header.action h1").text.strip()
    assert heading == "Travel"

    # All prices on the page should show GBP symbol
    prices = [e.text.strip() for e in driver.find_elements(By.CSS_SELECTOR, "article.product_pod p.price_color")]
    assert prices, "Expected at least one price"
    assert all(p.startswith("£") for p in prices)

    # URL sanity check contains category slug
    assert "travel_2" in driver.current_url
