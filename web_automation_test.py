"""
This code automated the login and transaction counting using Selenium and Pytest
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

DEMO_LOGIN_URL = "https://demo.applitools.com/"
USERNAME = "testuser"
PWD = "password123"
BROWSER_TIMEOUT = 10
EXPECTED_COMPLETED_TRANSACTIONS = 2  # there are 2 successful status, not 3 as mentioned in the assignment doc.


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.get(DEMO_LOGIN_URL)
    yield driver
    driver.quit()


def test_login_and_successful_transactions(browser):
    # login data
    # username_field = browser.find_element(By.ID, "username")
    username_field = WebDriverWait(browser, BROWSER_TIMEOUT).until(
        ec.presence_of_element_located((By.ID, "username")))
    password_field = browser.find_element(By.ID, "password")
    signin_btn = browser.find_element(By.ID, "log-in")

    # Provide credentials and login
    username_field.send_keys(USERNAME)
    password_field.send_keys(PWD)
    signin_btn.click()

    # Wait for the transactions table to appear (assuming a successful login redirects to the table)
    WebDriverWait(browser, BROWSER_TIMEOUT).until(ec.presence_of_element_located((By.XPATH, "//table")))
    transaction_table = browser.find_element(By.XPATH, "//table")
    # success_count = transaction_table.text.count('Complete')
    rows = transaction_table.find_elements(By.TAG_NAME, "tr")
    success_count = 0

    for row in rows:
        status = row.text.split(" ")[0]
        if status == "Complete":  # indicates on a successful status
            success_count += 1

    assert success_count == EXPECTED_COMPLETED_TRANSACTIONS


if __name__ == "__main__":
    try:
        pytest.main()
    except Exception as e:
        print(f'The following error occurred:\n{e}')
    finally:
        print("Test Over!")



