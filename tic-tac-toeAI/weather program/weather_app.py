import requests
import json
from datetime import datetime

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use metric units (Celsius)
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        
        # Extract relevant weather information
        weather_data = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"],
            "sunrise": datetime.fromtimestamp(data["sys"]["sunrise"]).strftime('%H:%M:%S'),
            "sunset": datetime.fromtimestamp(data["sys"]["sunset"]).strftime('%H:%M:%S')
        }
        
        return weather_data
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def main():
    print("Welcome to the Weather Program!")
    print("-------------------------------")
    
    # Get API key from user
    api_key = input("Please enter your OpenWeatherMap API key: ")
    city = input("Enter the city name: ")
    
    weather_data = get_weather(api_key, city)
    
    if weather_data:
        print("\nWeather Information:")
        print("-------------------")
        print(f"City: {weather_data['city']}")
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Feels like: {weather_data['feels_like']}°C")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Weather: {weather_data['description'].capitalize()}")
        print(f"Wind Speed: {weather_data['wind_speed']} m/s")
        print(f"Sunrise: {weather_data['sunrise']}")
        print(f"Sunset: {weather_data['sunset']}")
    else:
        print("Failed to fetch weather data. Please check your API key and city name.")

if __name__ == "__main__":
    main() 