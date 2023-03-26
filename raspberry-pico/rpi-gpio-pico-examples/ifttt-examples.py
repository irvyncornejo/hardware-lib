from gpiopico import Network
from config import ssid, password #create config file with ssid and password

http = Network(ssid, password) #create wlan config and have http methods

"""
raspberry pico-w -> ifttt(webhook) -> spreadsheets (write values)
"""

url = '' #ifttt endpoint

response = http.post(
    url=url,
    headers={"content-type": "application/json"},
    body={"value1":"567","value2":"890"},
    format_response='text'
)

print(response)
