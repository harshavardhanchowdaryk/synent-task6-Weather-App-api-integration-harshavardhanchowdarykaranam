import requests

# Enter your OpenWeatherMap API key here
api_key = "YOUR_API_KEY"

# Take city name from user
city = input("Enter city name: ")

# API URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# Send request to API
response = requests.get(url)

# Convert response to JSON format
weather_data = response.json()

# Check if city exists and request is successful
if str(weather_data.get("cod")) == "200":

    temperature = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]

    print("\nWeather Information")
    print("--------------------")
    print("City:", city)
    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")

else:
    print("Unable to fetch weather information.")
    print("Reason:", weather_data.get("message", "Unknown error"))