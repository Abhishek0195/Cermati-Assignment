import pytest
from webdriverio import WebDriver

@pytest.fixture(scope='session')
def driver():
    # Set up WebDriver here
    driver = WebDriver()

    # Start the WebDriver session
    driver.start()

    yield driver

    # End the WebDriver session
    driver.stop()

def test_apply_filters(driver):
    # Go to www.ebay.com
    driver.url('https://www.ebay.com')

    # Navigate to Search by category > Electronics > Cell Phones & accessories
    driver.click('[data-testid="search-category-dropdown-toggle"]')
    driver.click('Electronics')
    driver.click('Cell Phones & accessories')

    # After the page loads, click Cell Phones & Smartphones in the left-hand side navigation section.
    driver.click('Cell Phones & Smartphones')

    # Now, click – See All (appears under “Shop by brand” or “Shop by Network”).
    driver.click('See All')

    # Add 3 filters - screen size, Price, and Item location appearing in the pop-up and click apply.
    driver.click('Screen Size')
    driver.click('Price')
    driver.click('Item Location')
    driver.click('Apply')

    # Verify that the filter tags are applied
    assert driver.isDisplayed('.filter-tag-item')

    # Additional assertions or verifications can be added as needed

