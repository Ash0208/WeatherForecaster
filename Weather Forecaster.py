import datetime as dt
import requests

# Base URL components
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "-Input API Key Here-"  #input api key
CITY = "Jakarta"    #input city with capital letter

# Temperature converter
def temp_k_to_c_f(kelvin):
    celsius = kelvin -273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

# Construct the API request URL
url = f"{BASE_URL}q={CITY}&appid={API_KEY}"

# Send the request and get the response
data = requests.get(url)


if data.status_code == 200:
    response = data.json()
    
    # Extract weather data
    temp_k = response['main']['temp']
    temp_c, temp_f = temp_k_to_c_f(temp_k)
    feels_like_k = response['main']['feels_like']
    feels_like_c, feels_like_f = temp_k_to_c_f(feels_like_k)
    wind_speed = response['wind']['speed']
    humidity  = response['main']['humidity']
    desc = response['weather'][0]['description']

    # Convert sunrise & sunset times correctly
    timezone_offset = response['timezone']  # Timezone offset in seconds
    sunrise_utc = dt.datetime.fromtimestamp(response['sys']['sunrise'], dt.timezone.utc)
    sunset_utc = dt.datetime.fromtimestamp(response['sys']['sunset'], dt.timezone.utc)

    # Apply timezone offset
    sunrise_local = sunrise_utc + dt.timedelta(seconds=timezone_offset)
    sunset_local = sunset_utc + dt.timedelta(seconds=timezone_offset)

    # Print weather information
    print(f"Temperature in {CITY}: {temp_c:.2f}°C or {temp_f:.2f}°F")
    print(f"Temperature in {CITY} feels like: {feels_like_c:.2f}°C or {feels_like_f:.2f}°F")
    print(f"Humidity in {CITY}: {humidity}%")
    print(f"Wind speed in {CITY}: {wind_speed}m/s")
    print(f"General weather in {CITY}: {desc}")
    print(f"Sun rises in {CITY} at {sunrise_local} local time")
    print(f"Sun sets in {CITY} at {sunset_local} local time")

else:
    print(f"Error: Unable to fetch weather data (Status Code: {data.status_code})")