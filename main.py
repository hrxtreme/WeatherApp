import requests
import json

city = input("Enter your city: ")

# url = f"https://api.weatherapi.com/v1/current.json?key=31b4fbc157e24eba841112733232712&q={city}&aqi=yes"
url = f"https://api.weatherapi.com/v1/current.json?key=31b4fbc157e24eba841112733232712&q={city}&aqi=yes"

r = requests.get(url)
# print(json.dumps(r.json(), separators=(",",":"), indent=4))

weatherdict = json.loads(r.text)
print(f"Current temp is: {weatherdict['current']['temp_c']}°C")
aqi = weatherdict['current']['air_quality']
print(f"Air quality index is: {aqi}")


# Chat gpt response

# import requests
#
# def get_weather_data(city):
#     api_key = "31b4fbc157e24eba841112733232712"
#     url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=yes"
#
#     try:
#         response = requests.get(url)
#         response.raise_for_status()  # Raise an exception if the request fails
#         weather_data = response.json()
#         return weather_data
#     except requests.RequestException as e:
#         print(f"Error fetching weather data: {e}")
#         return None
#
# def display_weather_info(weather_data):
#     if weather_data:
#         current_temp_c = weather_data['current']['temp_c']
#         aqi = weather_data['current']['air_quality']
#
#         print(f"Current temperature: {current_temp_c}°C")
#         print(f"Air quality index: {aqi}")
#     else:
#         print("Unable to retrieve weather data. Please check your city name and try again.")
#
# def main():
#     city = input("Enter your city: ")
#     weather_data = get_weather_data(city)
#     display_weather_info(weather_data)
#
# if __name__ == "__main__":
#     main()
