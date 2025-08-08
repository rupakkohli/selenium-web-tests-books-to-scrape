# Selenium Web Tests – Books to Scrape

A learning project where Python and Selenium are being used for UI automation.  
I’m using [BooksToScrape.com](https://books.toscrape.com/) as a safe, static test site.

---

## Tests so far

- **Homepage title test** – my first Selenium script; checks that the title contains “Books to Scrape”.
- **Travel category test** – clicks the category, checks heading text, GBP currency symbol, and URL.
- **Science category pagination test** – written to click “Next” in a category, but currently skipped because Science only has one page.  
  *(Keeping it in to show progress and next steps.)*

---

## Progress log

- Initial setup – Created Git repo, virtual environment, installed Selenium and Pytest, wrote homepage title test.
- Next – Added Travel category test with heading, currency, and URL checks.
- Latest – Added pagination test (skipped for now because category has only one page).

---

## Notes

- Learned how to set up Pytest fixtures for browser setup and teardown.
- Discovered that not all categories have pagination.
- Added `pytest.skip()` for realistic handling of missing features.
- Next up:  
  - Try pagination on a category with more than one page (for example, Poetry).  
  - Add HTML test reports.  
  - Run tests in GitHub Actions.

---

## How to run

```bash
pip install -r requirements.txt
pytest
