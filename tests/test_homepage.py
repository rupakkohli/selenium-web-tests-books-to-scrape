# tests/test_homepage.py
def test_homepage_title(driver):
    # Uses the driver fixture from conftest.py
    url = "https://books.toscrape.com/"
    driver.get(url)
    assert "Books to Scrape" in driver.title
