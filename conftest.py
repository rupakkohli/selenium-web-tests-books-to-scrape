# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    opts = Options()
    # Uncomment for CI/headless later:
    # opts.add_argument("--headless=new")
    with webdriver.Chrome(options=opts) as d:   # uses Selenium Manager to fetch driver
        d.set_window_size(1280, 900)
        yield d
