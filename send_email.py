from playwright.sync_api import sync_playwright
from dotenv import load_dotenv, find_dotenv
import os
import time

# Load environment variables from .env file
env_path = find_dotenv()
load_dotenv(env_path)

# Access env variables
email = os.getenv('gmail')
password = os.getenv('gmailPassword')
excel_file_path = os.environ.get('excel')

def navigate_to_gmail(p):
    browser = p.chromium.launch(headless=False)  # Set headless=True to run in background
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://mail.google.com/")
    return page, browser

def login_to_gmail(page, email, password):
    print(f"Email: {email}")  # Debug: Print email value
    print("Entering email address")
    page.get_by_label("Email or phone").fill(email)
    page.get_by_role("button", name="Next").click()
    time.sleep(5)  # Wait for the next page to load

    print("Entering password")
    page.get_by_label("Enter your password").fill(password)
    page.get_by_role("button", name="Next").click()
    time.sleep(10)  # Wait for the inbox to load

def compose_and_send_email(page, recipient, subject, body, attachment_path):
    print("Clicking Compose button")
    page.get_by_role("button", name="Compose").click()
    time.sleep(2)  # Wait for the compose window to appear

    print("Entering recipient email")
    page.get_by_label("To recipients").fill(recipient)
    
    print("Entering subject")
    page.get_by_placeholder("Subject").fill(subject)

    print("Entering email body")
    page.get_by_placeholder("Subject").press("Tab")
    page.get_by_role("textbox", name="Message Body").fill(body)

    if attachment_path:
        print(f"Attaching file: {attachment_path}")
        # Open file input dialog
        with page.expect_file_chooser() as fc_info:
            page.get_by_label("Attach files").click()
        file_chooser = fc_info.value
        file_chooser.set_files(attachment_path)
        time.sleep(5)  # Wait for the attachment to upload

    print("Clicking Send button")
    page.get_by_label("Send", exact=True).click()
    time.sleep(5)  # Wait for the email to send

if __name__ == "__main__":
    if email is None or password is None:
        print("Error: Missing email or password in environment variables.")
        print(f"email: {email}, password: {password}")
    else:
        with sync_playwright() as p:
            page, browser = navigate_to_gmail(p)
            login_to_gmail(page, email, password)

            # Define email details
            recipient = email  # Replace with actual recipient
            subject = "Automated Email"
            body = "This is an automated email sent using Playwright."
            attachment_path = excel_file_path  # Replace with actual file path

            compose_and_send_email(page, recipient, subject, body, attachment_path)

            # Keep the browser open for further steps
            print("Email sent successfully. Keeping the browser open for further steps...")
            time.sleep(15)
            #input("Press Enter to close the browser...")
            browser.close()
