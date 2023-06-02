Test Script for eBay Website
This repository contains a test script written in Python using the pytest framework and the WebDriverIO library for automating tests on the eBay website. The script focuses on the scenario of accessing a product via category after applying multiple filters.

Prerequisites
Before running the test script, ensure that you have the following dependencies installed:

Python
pytest
webdriver.io
Web driver specific to your chosen browser (e.g., ChromeDriver)
Setup
Clone this repository or extract the provided zipped folder to your local machine.

Install the required Python packages by running the following command in the project's root directory:

Copy code
pip install -r requirements.txt
Make sure you have the appropriate web driver installed for your preferred browser (e.g., ChromeDriver) and added to your system's PATH.

Running the Test
To execute the test script, follow these steps:

Open a terminal or command prompt and navigate to the project's root directory.

Run the following command:

Copy code
pytest test_script.py
This will run the test script and display the test results in the terminal.

Test Scenario
The test script focuses on the following scenario:

Scenario 1: Access a Product via category after applying multiple filters

Go to www.ebay.com.

Navigate to Search by category > Electronics > Cell Phones & accessories.

After the page loads, click Cell Phones & Smartphones in the left-hand side navigation section.

Click "See All" (appears under "Shop by brand" or "Shop by Network").

Add 3 filters - screen size, Price, and Item location appearing in the pop-up, and click apply.

Verify that the filter tags are applied.

Script Description
The test script (test_script.py) uses the pytest framework along with the WebDriverIO library for automating the test steps.

The script contains the following:

A fixture named driver that sets up and tears down the WebDriver session using the WebDriverIO library.

A test function named test_apply_filters that performs the test steps for the given scenario.

The test steps include navigating to the eBay website, selecting the desired category, applying filters, and verifying the applied filters.

Customization
To customize the test script for your specific environment or requirements, you may need to modify the WebDriver setup code in the driver fixture based on your chosen browser and WebDriver library.