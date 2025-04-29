import requests


def get_weather_forecast(latitude, longitude):
   """
   Fetches daily forecast data from the Open-Meteo API.
  
   Parameters:
       latitude (float): Latitude of the location.
       longitude (float): Longitude of the location.
  
   Returns:
       dict: JSON data returned by the API.
   """
   url = "https://api.open-meteo.com/v1/forecast"
   params = {
       "latitude": latitude,
       "longitude": longitude,
       # Request daily weather code and temperature extremes.
       "daily": "weathercode,temperature_2m_max,temperature_2m_min",
       # Setting the timezone to ensure the dates match your local time.
       "timezone": "Europe/Berlin"
   }
  
   response = requests.get(url, params=params)
   response.raise_for_status()  # Raise an exception for HTTP errors
   return response.json()


def get_icon_for_weathercode(code):
   """
   Maps an Open-Meteo weather code to an emoji icon.
  
   Weather codes (according to Open-Meteo documentation) are interpreted as:
     - 0: Clear sky
     - 1, 2, 3: Mainly clear, partly cloudy, and overcast
     - 45, 48: Fog and depositing rime fog
     - 51, 53, 55: Drizzle
     - 56, 57: Freezing drizzle
     - 61, 63, 65: Rain
     - 66, 67: Freezing rain
     - 71, 73, 75: Snow fall
     - 77: Snow grains
     - 80, 81, 82: Rain showers
     - 85, 86: Snow showers
     - 95: Thunderstorm
     - 96, 99: Thunderstorm with hail
  
   Parameters:
       code (int): The weather code.
  
   Returns:
       str: An emoji representing the weather.
   """
   if code == 0:
       return "☀️"  # Clear sky
   elif code in [1, 2, 3]:
       return "🌤"  # Mainly clear, partly cloudy, overcast
   elif code in [45, 48]:
       return "🌫"  # Fog
   elif code in [51, 53, 55]:
       return "🌦"  # Drizzle
   elif code in [56, 57]:
       return "🥶"  # Freezing drizzle
   elif code in [61, 63, 65]:
       return "🌧"  # Rain
   elif code in [66, 67]:
       return "❄️"  # Freezing rain
   elif code in [71, 73, 75]:
       return "❄️"  # Snow fall
   elif code == 77:
       return "❄️"  # Snow grains
   elif code in [80, 81, 82]:
       return "🌦"  # Rain showers
   elif code in [85, 86]:
       return "❄️"  # Snow showers
   elif code == 95:
       return "⛈"  # Thunderstorm
   elif code in [96, 99]:
       return "🌩"  # Thunderstorm with hail
   else:
       return "🌈"  # Default icon


def main():
   # Coordinates for Berlin (adjust as needed)
   latitude = 52.52
   longitude = 13.41
  
   # Fetch the forecast data
   forecast_data = get_weather_forecast(latitude, longitude)
   daily = forecast_data.get("daily", {})
  
   # Make sure we received the expected data
   if not daily:
       print("No daily forecast data available.")
       return
  
   # Assuming index 0 is today's forecast and index 1 is tomorrow's forecast.
   tomorrow_index = 1
  
   # Retrieve tomorrow's weather code and temperatures.
   try:
       weather_code = daily["weathercode"][tomorrow_index]
       temp_max = daily["temperature_2m_max"][tomorrow_index]
       temp_min = daily["temperature_2m_min"][tomorrow_index]
   except (IndexError, KeyError) as e:
       print("Error processing forecast data:", e)
       return
  
   # Get the corresponding weather icon.
   icon = get_icon_for_weathercode(weather_code)
  
   # Display the forecast.
   print("Tomorrow's Forecast for Berlin:")
   print(f"Weather Code: {weather_code} {icon}")
   print(f"Temperature: High {temp_max}°C, Low {temp_min}°C")


# Run the main function
main()

