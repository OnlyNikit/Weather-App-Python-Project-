import requests
import os
from dotenv import load_dotenv



# !│
# !├── 1. Input Module
# !│      └── Get city name
# !│
# !├── 2. Validation Module
# !│      └── Check if input is valid
# !│
# !├── 3. Request Builder
# !│      └── Build the API URL/parameters
# !│
# !├── 4. API Communication
# !│      └── Send GET request
# !│
# !├── 5. Response Validation
# !│      └── Check status code
# !│
# !├── 6. Data Extraction
# !│      └── Extract temperature, humidity, etc.
# !│
# !├── 7. Presentation Layer
# !│      └── Print formatted output
# !│
# !└── 8. Error Handling
# !       └── Handle failures gracefully




# !-----------------------------------Taking Input ---------------------------------------------------------------------

def get_city():
    while True:
        cityName = input("Enter the city Name:")

        if not cityName:
            print("City name cannot be empty")
            continue
        
        if not cityName.isalpha():
            print("Enter Vaild city Name")
            continue

        return cityName
    

def fetch_weather(city):
    load_dotenv()
    base_url="http://api.openweathermap.org/data/2.5/weather"
    api_key=os.getenv("API_KEY")
    params={
        "q":city,
        "appid":api_key,
        "units":"metric"
    }

    try:
        response = requests.get(base_url,params=params,timeout=20)
        response.raise_for_status();
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error:",{e})
        return None

weatherData = fetch_weather("delhi")

def extract_data(weatherData):
        
        if weatherData is None:
            return None
        return {
        "city":weatherData["name"],
        "temperature" : weatherData["main"]["temp"],
        "humidity" : weatherData["main"]["humidity"],
        "description":weatherData["weather"][0]["description"],
        "windspeed":weatherData["wind"]["speed"],
        "feels_like":weatherData["main"]["feels_like"],
        "pressure":weatherData["main"]["pressure"],
        "visibility":weatherData["visibility"],
        }

weather= extract_data(weatherData)


def display_weather(weather):
    if weather is None:
        print("unable to fetch weather data")
        return
    
    print("\n=================== Weather Report =========================")
    print(f"city                        :{weather['city']}")
    print(f"temperature                 :{weather['temperature']} °C")
    print(f"humidity                    :{weather['humidity']}")
    print(f"feels_like                  :{weather['feels_like']}")
    print(f"description                 :{weather['description']}")
    print(f"wind_speed                  :{weather['windspeed']} m/s")
    print(f"pressure                    :{weather['pressure']}")
    print(f"visibility                  :{weather['visibility']}")

def main():
    city = get_city()
    weatherData=fetch_weather(city)
    weather=extract_data(weatherData)
    display_weather(weather)


main()
    


