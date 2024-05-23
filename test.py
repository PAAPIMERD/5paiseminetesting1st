from py5paisa import FivePaisaClient
cred={
    "APP_NAME":"5P50289032",
    "APP_SOURCE":"22145",
    "USER_ID":"jv0zaXaW7lD",
    "PASSWORD":"ZusnUUqsJoh",
    "USER_KEY":"24BLhwIxzMHo31rotJYypWuvYUU4mCHZ",
    "ENCRYPTION_KEY":"FanCs8NKjzunmTmGXgxkOPYS5QUwsXvU"
    }
client = FivePaisaClient(cred=cred)
client.get_oauth_session('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6IjUwMjg5MDMyIiwicm9sZSI6IjI0Qkxod0l4ek1IbzMxcm90Sll5cFd1dllVVTRtQ0haIiwiU3RhdGUiOiIiLCJuYmYiOjE3MTY0ODQ5OTgsImV4cCI6MTcxNjQ4ODU5OCwiaWF0IjoxNzE2NDg0OTk4fQ.OWJsXSfDu7ZEWIhbcm8fgt9UK6Y_kB6EJB73jD4Yk50')
#NOTE : ScripData and ScripCode you can find from new Scripmaster as mentioned above
import time

req_list_ = [{"Exch": "N", "ExchType": "C", "ScripData": "ITC_EQ"}]
x=0

print(client.fetch_market_feed_scrip(req_list_))

while True:
  
  x+=1
  print(client.fetch_market_feed_scrip(req_list_))
  print(x)


