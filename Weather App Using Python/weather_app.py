import requests
import json

# Function to fetch the weather
def get_weather(city, api_key):
    # OpenWeatherMap API URL with city and API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    # Sending a GET request to fetch the weather data
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        # Extracting necessary information from the response
        city_name = data["name"]
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        
        # Print the weather information
        print(f"Weather in {city_name}:")
        print(f"Description: {weather}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hPa")
    else:
        print("Error: Unable to fetch weather data. Please check the city name or API key.")
# def get_weather(city, api_key):
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
#     response = requests.get(url)
    
#     # Debug: Check status code and response
#     print(f"Status Code: {response.status_code}")  # Check status code
#     print(f"Response Text: {response.text}")        # Print the full error message from the API

#     if response.status_code == 200:
#         data = response.json()
#         city_name = data["name"]
#         weather = data["weather"][0]["description"]
#         temperature = data["main"]["temp"]
#         humidity = data["main"]["humidity"]
#         pressure = data["main"]["pressure"]

#         print(f"Weather in {city_name}:")
#         print(f"Description: {weather}")
#         print(f"Temperature: {temperature}°C")
#         print(f"Humidity: {humidity}%")
#         print(f"Pressure: {pressure} hPa")
#     else:
#         print("Error: Unable to fetch weather data. Please check the city name or API key.")

# Main function to take user input
def main():
    api_key = "8d27a5c1160c8d91fd963a5d430f0724"  # Replace with your OpenWeatherMap API Key
    city = input("Enter city name: ")
    
    get_weather(city, api_key)

# Run the application
if __name__ == "__main__":
    main()
