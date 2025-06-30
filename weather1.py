import requests

api_key = "13b1830543de496493b16d2ecf69f283"
lat1, lon1 = -39.610411497009196, -54.48267357289278
lat2, lon2 = -61.53254, -38.53225
lat3, lon3 = -83.2537125,  -44.2763782

def weather_res(lat: float,lon: float):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url)
    print(response.status_code)
    data = response.json()
    print(data)

def weather_city(city: str):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    print(response.status_code)
    data = response.json()
    print(data)


# weather_res(30.751, 46.288)
# weather_res(lat1, lon1)
# weather_res(lat2, lon2)
# weather_res(lat3, lon3)
weather_city("buenos aires")