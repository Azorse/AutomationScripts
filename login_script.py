from playwright.sync_api import sync_playwright

def run(playwright):
    # Launch the browser
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    # Navigate to the login page
    page.goto('https://simworks.safetyinmotion.com/#/log-in')
    # Fill in the username and password fields
    page.fill('input[placeholder="Email"]', 'dan')
    page.fill('input[placeholder="Password"]', 'Skeejah#8440')
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