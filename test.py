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
    #print("Session Token:", session_token)

    # Generate OAuth session
    oauth_token = client.get_oauth_session(session_token)
    #print("OAuth Token:", oauth_token)

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
def get_last_rate(market_feed):
    """
    Extracts and returns the 'LastRate' from the market feed data.

    Parameters:
        market_feed (dict): A dictionary containing market feed data.

    Returns:
        float: The LastRate value from the market feed data.
    """
    # Check if the market feed is successful and has data
    if market_feed['Status'] == 0 and 'Data' in market_feed and len(market_feed['Data']) > 0:
        # Return the 'LastRate' from the first item in the data list
        return market_feed['Data'][0]['LastRate']
    else:
        # Return None if no data is found or there's an error in the feed
        return None
















# Fetch market feed
print(client.fetch_market_feed_scrip(req_list_))

while True:
    x += 1


    data = get_last_rate(client.fetch_market_feed_scrip(req_list_))
    data = str(data)
    if data is None:
      oauth_token = generate_session_and_oauth(client_code, pin)
      client.get_oauth_session(oauth_token)
      data = get_last_rate(client.fetch_market_feed_scrip(req_list_))
      data = str(data)

    print(data)




    
    print(x)
