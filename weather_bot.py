import time
import requests
from plyer import notification

# 1. Set your location coordinates (Latitude & Longitude)
# Example coordinates (Change these to your city's lat/lon!):
LATITUDE = 25.79  
LONGITUDE = 55.98 

# 2. Build the Open-Meteo API URL
WEATHER_URL = f"https://api.open-meteo.com/v1/forecast?latitude={LATITUDE}&longitude={LONGITUDE}&current_weather=true"

def check_weather_and_notify():
    try:
        # Fetch the live weather JSON data from the web
        response = requests.get(WEATHER_URL)
        data = response.json()
        
        # Extract current temperature and weather status code
        current_temp = data["current_weather"]["temperature"]
        weather_code = data["current_weather"]["weathercode"]
        
        # Determine condition (WMO codes: 0 = Clear, 1-3 = Cloudy, 51+ = Rain/Snow)
        if weather_code == 0:
            status = "Sunny / Clear Sky"
        elif weather_code in [1, 2, 3]:
            status = "Partly Cloudy"
        elif weather_code >= 51:
            status = "Rainy or Stormy"
        else:
            status = "Moderate Conditions"

        # Create the message text
        title_text = "🌤️ Daily Weather Update"
        message_text = f"Current Temp: {current_temp}°C\nCondition: {status}"
        
        # Trigger the native desktop notification
        notification.notify(
            title=title_text,
            message=message_text,
            app_name="Weather Bot",
            timeout=10  # Seconds the popup stays on screen
        )
        print("Notification sent successfully!")

    except Exception as e:
        print(f"Failed to fetch weather: {e}")

# Run the function once immediately when you execute the script
if __name__ == "__main__":
    check_weather_and_notify()