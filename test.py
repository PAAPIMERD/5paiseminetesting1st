from py5paisa import FivePaisaClient
import pyotp
import time

# Credentials for FivePaisaClient
cred = {
    "APP_NAME": "5P50289032",
    "APP_SOURCE": "22145",
    "USER_ID": "jv0zaXaW7lD",
    "PASSWORD": "ZusnUUqsJoh",
    "USER_KEY": "24BLhwIxzMHo31rotJYypWuvYUU4mCHZ",
    "ENCRYPTION_KEY": "FanCs8NKjzunmTmGXgxkOPYS5QUwsXvU"
}

# Initialize the FivePaisa client
client = FivePaisaClient(cred=cred)

# Replace 'YOUR_TOTP_SECRET' with your actual TOTP secret key
totp_secret = 'GUYDEOBZGAZTEXZVKBDUWRKZ'  # Ensure this is a valid base32 string
totp = pyotp.TOTP(totp_secret)

def generate_session_and_oauth(client_code, pin):
    current_totp = totp.now()
    print("Current TOTP:", current_totp)

    # Generate TOTP session
    session_token = client.get_totp_session(client_code, current_totp, pin)
    print("Session Token:", session_token)

    # Generate OAuth session
    oauth_token = client.get_oauth_session(session_token)
    print("OAuth Token:", oauth_token)
    
    return oauth_token

# Replace 'Your ClientCode' and 'Your Pin' with actual values
client_code = '50289032'
pin = '271707'

# Generate the OAuth token
oauth_token = generate_session_and_oauth(client_code, pin)

# Replace the static OAuth token with the dynamically generated one in client initialization
client.get_oauth_session(oauth_token)

# ScripData and ScripCode
req_list_ = [{"Exch": "N", "ExchType": "C", "ScripData": "ITC_EQ"}]
x = 0

# Fetch market feed
print(client.fetch_market_feed_scrip(req_list_))

while True:
    x += 1
    oauth_token = generate_session_and_oauth(client_code, pin)
    client.get_oauth_session(oauth_token)

    print(client.fetch_market_feed_scrip(req_list_))
    print(x)

