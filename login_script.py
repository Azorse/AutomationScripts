from playwright.sync_api import sync_playwright
import os
import time
from dotenv import load_dotenv

#load env variables
load_dotenv()

#access env variables
email = os.environ.get('email')
password = os.environ.get('pwd')

def run(playwright):
    # Launch the browser
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    # Navigate to the login page
    page.goto('https://simworks.safetyinmotion.com/#/log-in')
    # Fill in the username and password fields
    page.fill('input[placeholder="Email"]', email)
    page.fill('input[placeholder="Password"]', password)
    # Click the login button
    page.click('button[type="submit"]')
    # Wait for navigation to complete
    page.wait_for_load_state("networkidle")
    # Optionally, print the title of the new page to verify login
    print(page.title())
    # Close the browser
    browser.close()
with sync_playwright() as playwright:
    run(playwright)