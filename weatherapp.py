import requests

api_key = "83709ba3b024363a9610b59ef363abce"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

print("Status Code:", response.status_code)

weather_data = response.json()

print("API Response:")
print(weather_data)

if str(weather_data.get("cod")) == "200":

    temperature = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]

    print("\nWeather Information")
    print("--------------------")
    print("City:", city)
    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")

else:
    print("\nUnable to fetch weather information.")
    print("Reason:", weather_data.get("message"))