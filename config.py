import os

USE_ROUNDED_COORDS = False
IP_INFO_URL = "https://ipinfo.io/json"
OPENWEATHER_API = os.environ.get("OPEN_WEATHER_API_KEY")
OPENWEATHER_URL = (
    "https://api.openweathermap.org/data/2.5/weather?"
    "lat={latitude}&lon={longitude}&"
    "appid=" + OPENWEATHER_API + "&lang=ru&"
    "units=metric"
)
