import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Replace 'your_webhook_url' with your actual Discord webhook URL
DISCORD_WEBHOOK_URL = 'your_webhook_url'

def fetch_gas_price():
    # Replace 'vendor_page_url' with the URL of the page you want to gather info from. make sure you have permission
    url = 'vendor_page_url'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Modify the selector based on how the price is displayed on the vendor's page
    price_element = soup.find('your_selector_for_price')
    if price_element:
        return price_element.text.strip()  # Adjust this based on the page structure
    return "Price not found."

def send_discord_notification(message):
    data = {"content": message}
    response = requests.post(DISCORD_WEBHOOK_URL, json=data)
    print("Notification sent, status code:", response.status_code)

if __name__ == "__main__":
    price = fetch_gas_price()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"Gas Price Update - {now}: {price}"
    send_discord_notification(message)
