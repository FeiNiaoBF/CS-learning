import requests
import json

def main():
    print(get_weather())

def get_weather():
    api_key = '58b580274f99f5ef26062af1dc4cbb88'
    city = 'Kunming'
    print(api_key)
    print(city)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    response = requests.get(url)
    data = json.dumps(response.json(), indent=4)
    return data

main()
