import requests
from settings import OW_API_ENDPOINT, OW_UNITS, OW_API_KEY, CIRCUS_LOCATION


def get_weather_forecast(city):
    url = str.format("{0}?units={1}&APPID={2}&q={3}",
                     OW_API_ENDPOINT,
                     OW_UNITS,
                     OW_API_KEY,
                     city)

    # Sample Open Weather API Response:
    '''
    {
        "coord": {
            "lon": -122.04,
            "lat": 37.37
        },
        "weather": [
            {
                "id": 502,
                "main": "Rain",
                "description": "heavy intensity rain",
                "icon": "10n"
            },
            {
                "id": 701,
                "main": "Mist",
                "description": "mist",
                "icon": "50n"
            }
        ],
        "base": "cmc stations",
        "main": {
            "temp": 54.07,
            "pressure": 1020,
            "humidity": 76,
            "temp_min": 50,
            "temp_max": 57.2
        },
        "wind": {
            "speed": 5.82,
            "deg": 270
        },
        "rain": {
            "1h": 13.21
        },
        "clouds": {
            "all": 1
        },
        "dt": 1461391038,
        "sys": {
            "type": 1,
            "id": 471,
            "message": 0.013,
            "country": "US",
            "sunrise": 1461417705,
            "sunset": 1461466285
        },
        "id": 5400075,
        "name": "Sunnyvale",
        "cod": 200
    }
    '''

    response = requests.get(url)
    weather_json = response.json()

    description = weather_json["weather"][0]["description"]
    current_temp = weather_json["main"]["temp"]
    min_temp = weather_json["main"]["temp_min"]
    max_temp = weather_json["main"]["temp_max"]

    forecast = str.format(("The current temp at the Circus in {0} is {1}. "
                           "Forecast for today is \"{2}\" with a high "
                           "of {3} and a low of {4}."),
                          CIRCUS_LOCATION,
                          int(current_temp),
                          description,
                          int(max_temp),
                          int(min_temp))

    return forecast
