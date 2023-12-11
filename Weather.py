import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            print("\n===== Weather Information =====")
            print(f"City: {data['name']}")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Weather: {data['weather'][0]['description']}")
            print(f"Wind Speed: {data['wind']['speed']} m/s")
        else:
            print(f"Error: {data['message']}")

    except Exception as e:
        print(f"Error: {e}")

def main():
    print("Welcome to the Simple Weather App!")
    api_key = input("Enter your OpenWeatherMap API key: ")
    city = input("Enter the city name: ")

    get_weather(api_key, city)

if __name__ == "__main__":
    main()
#  API key: 549b4e146d344a637bc5ea6a3f95c39c
# git init
# git add Weather.py
# git commit -m "Weather.py"
# git push origin main