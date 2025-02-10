# Weather Data Fetcher

## Overview
This Python script retrieves and displays current weather data for a specified city using the OpenWeatherMap API. It provides temperature (in Celsius and Fahrenheit), humidity, wind speed, general weather description, and sunrise/sunset times adjusted to the local timezone.

## Features
- Fetches real-time weather data using OpenWeatherMap API.
- Converts temperature from Kelvin to Celsius and Fahrenheit.
- Retrieves humidity, wind speed, and general weather conditions.
- Computes sunrise and sunset times based on local timezone.

## Dependencies
- Python 3.x
- `requests` library

## Installation & Usage
1. **Install Dependencies:**
   ```bash
   pip install requests
   ```
2. **Set Up API Key:**
   - Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api).
   - Replace `-Input API Key Here-` with your actual API key in the script.

3. **Modify City Name (Optional):**
   - Update the `CITY` variable to fetch weather data for a different location.

4. **Run the Script:**
   ```bash
   python weather_fetcher.py
   ```
   - The script will display the weather details in the terminal.

## Limitations
- Requires a valid API key from OpenWeatherMap.
- API may have rate limits depending on the subscription plan.
- Internet connection is required to fetch data.
- Limited to the OpenWeatherMap free tier's available data.

## Disclaimer
This script is intended for educational and personal use only. Ensure compliance with OpenWeatherMap's terms of service when using the API.

