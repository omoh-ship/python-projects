import requests
import os
from twilio.rest import Client
# To launch on python everywhere server
# from twilio.http.http_client import TwilioHttpClient
# import os

api_key = os.environ['OPEN_WEATHER_API_KEY']
ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
MY_LAT = 9.076479
MY_LONG = 7.398574

account_sid = os.environ['ACCOUNT_SID']
auth_token = os.environ['AUTH_TOKEN']

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,daily,minutely"
}

response = requests.get(url=ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
hourly = weather_data["hourly"]
hourly = hourly[:12]

will_rain = False

for item in hourly:
    weather_id = hourly[0]["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True

if will_rain:
    # Still for pythoneverywhere launching
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {"https": os.environ["https_proxy"]}
    # client = Client(account_sid, auth_token, http_client=proxy_client)
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☂.",
        from_="+12178852612",
        to="+1 345678962"
    )

    print(message.status)

