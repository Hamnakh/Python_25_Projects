# Weather Program

A simple Python program that fetches weather information for any city using the OpenWeatherMap API.

## Features

- Get current weather information for any city
- Display temperature, humidity, wind speed, and more
- Show sunrise and sunset times
- Uses metric units (Celsius)

## Requirements

- Python 3.x
- requests library

## Installation

1. Clone this repository or download the files
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Getting Started

1. Sign up for a free API key at [OpenWeatherMap](https://openweathermap.org/api)
2. Run the program:
   ```
   python weather_app.py
   ```
3. Enter your API key when prompted
4. Enter the city name you want to check the weather for

## Example Output

```
Welcome to the Weather Program!
-------------------------------
Please enter your OpenWeatherMap API key: your_api_key_here
Enter the city name: London

Weather Information:
-------------------
City: London
Temperature: 15.5°C
Feels like: 14.2°C
Humidity: 65%
Weather: Cloudy
Wind Speed: 3.2 m/s
Sunrise: 06:45:23
Sunset: 18:30:45
```

## Note

Make sure to keep your API key secure and don't share it publicly. 