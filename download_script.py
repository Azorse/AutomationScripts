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
    # define the download dir
    download_dir = os.path.join(os.getcwd(), 'downloads')
    os.makedirs(download_dir, exist_ok=True)

    # Launch the browser
    browser = playwright.chromium.launch_persistent_context(
        user_data_dir='/tmp/playwright',
        headless=False,
        accept_downloads=True
    )

    #Open browser
    page = browser.new_page()

    # Navigate to the login page
    page.goto('https://simworks.safetyinmotion.com/#/log-in')

    # Fill in the username and password fields
    page.fill('input[placeholder="Email"]', email)
    page.fill('input[type="password"]', password)

    # Click the login button
    page.click('button[type="submit"]')

    # Wait for navigation to complete
    page.wait_for_load_state("networkidle")

    # Navigate to the target page
    page.goto('https://simworks.safetyinmotion.com/#/company/33/observations')

    # Click the filter button (using class names)
    page.click('div.control-btn.btn-green')

    # Wait for modal to appear
    page.wait_for_selector('a.bp3-menu-item')

    #Click the "Past Week" link
    page.click('a:has-text("Past week")')

    #Click the "Apply Filter" button
    page.click('button.btn-green:text("Apply filter")')

    #Wait for the page to load after applying filter
    page.wait_for_load_state("networkidle")

    #pause
    print("filter applied")
    time.sleep(5)

    # Ensure download directory
    download_dir = os.path.join(os.getcwd(), 'downloads')
    os.makedirs(download_dir, exist_ok=True)

    # Download the .csv file
    with page.expect_download() as download_info:
        page.click('div.control-btn.btn-green:text("Export")')  
    download = download_info.value
    download_path = os.path.join(download_dir, download.suggested_filename)
    print(f"downloading file to: {download_path}")
    download.save_as(download_path)

    #pause
    print("pausing for verification")
    time.sleep(30)

    # Close the browser
    browser.close()
with sync_playwright() as playwright:
    run(playwright)