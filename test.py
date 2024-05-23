from py5paisa import FivePaisaClient
client.get_oauth_session('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6IjUwMjg5MDMyIiwicm9sZSI6IjI0Qkxod0l4ek1IbzMxcm90Sll5cFd1dllVVTRtQ0haIiwiU3RhdGUiOiIiLCJuYmYiOjE3MTY0ODQ5OTgsImV4cCI6MTcxNjQ4ODU5OCwiaWF0IjoxNzE2NDg0OTk4fQ.OWJsXSfDu7ZEWIhbcm8fgt9UK6Y_kB6EJB73jD4Yk50')
#NOTE : ScripData and ScripCode you can find from new Scripmaster as mentioned above
import time

req_list_ = [{"Exch": "N", "ExchType": "C", "ScripData": "ITC_EQ"}]
x=0

print(client.fetch_market_feed_scrip(req_list_))

while True:
  time.sleep(1)
  x+=1
  print(client.fetch_market_feed_scrip(req_list_))
  print(x)


