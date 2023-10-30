# ControlAP_assignment
Home assignment: web automation test
To execute the automation script, follow these instructions:
Clone the GitHub repository to your local machine.
Ensure you have the necessary web driver (e.g., ChromeDriver) for your browser installed and added to your system's PATH.
Set the expected count value in the test script to the actual expected value.
Open a terminal and navigate to the project directory.
Run the test script using Pytest:
pytest web_automation_test.py

The script will open a browser, navigate to the provided URL, log in with the given credentials,
count the successful transactions, and assert the count against the expected value.
The browser will be closed automatically after the test is complete.
