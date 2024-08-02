import os
from dotenv import load_dotenv

print("Starting script...")

# Load .env file
env_path = '/Users/danschissler/AutomationScripts/.env'
print(f"Loading .env file from: {env_path}")
load_dotenv(dotenv_path=env_path)

# Access env variables
email = os.getenv('email')
password = os.getenv('pwd')
csv_file_path = os.getenv('csv')
excel_file_path = os.getenv('excel')

# Print the loaded values
print(f"Email: {email}")
print(f"Password: {password}")
print(f"CSV File Path: {csv_file_path}")
print(f"Excel File Path: {excel_file_path}")

# Check if CSV and Excel paths are loaded correctly
if csv_file_path is None:
    print("CSV file path is not loaded correctly from .env")
else:
    print("CSV file path is loaded correctly from .env")

if excel_file_path is None:
    print("Excel file path is not loaded correctly from .env")
else:
    print("Excel file path is loaded correctly from .env")
