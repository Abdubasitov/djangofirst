# weather.py
import requests

# Координаты городов (ключевая идея!)
CITIES = {
    "Манас": {"lat": 40.935423, "lon": 72.984933},
    "Бишкек": {"lat": 42.8746, "lon": 74.5698},
    "Ош": {"lat": 40.5333, "lon": 72.7833},
}

API_URL = "https://api.open-meteo.com/v1/forecast"

# Словарь для преобразования weathercode в текст
WEATHER_CODES = {
    0: "Ясно",
    1: "Частично облачно",
    2: "Облачно",
    3: "Пасмурно",
    45: "Туман",
    48: "Туман с инеем",
    51: "Морось",
    53: "Умеренная морось",
    55: "Сильная морось",
    56: "Снежная морось",
    57: "Сильная снежная морось",
    61: "Дождь",
    63: "Умеренный дождь",
    65: "Сильный дождь",
    66: "Лёд",
    67: "Сильный лёд",
    71: "Снег",
    73: "Умеренный снег",
    75: "Сильный снег",
    77: "Снежные хлопья",
    80: "Ливень",
    81: "Умеренный ливень",
    82: "Сильный ливень",
    95: "Гроза",
    96: "Гроза с градом",
    99: "Сильная гроза с градом"
}
# weather.py
WEATHER_ICONS = {
    0: "☀️",   # Ясно
    1: "🌤",   # Частично облачно
    2: "☁️",   # Облачно
    3: "🌥",   # Пасмурно
    45: "🌫",  # Туман
    48: "🌫❄️", # Туман с инеем
    51: "🌦",  # Морось
    53: "🌦",  # Умеренная морось
    55: "🌧",  # Сильная морось
    56: "🌨",  # Снежная морось
    57: "🌨",  # Сильная снежная морось
    61: "🌧",  # Дождь
    63: "🌧",  # Умеренный дождь
    65: "🌧",  # Сильный дождь
    66: "🧊",  # Лёд
    67: "🧊",  # Сильный лёд
    71: "❄️",  # Снег
    73: "❄️",  # Умеренный снег
    75: "❄️",  # Сильный снег
    77: "❄️",  # Снежные хлопья
    80: "🌧",  # Ливень
    81: "🌧",  # Умеренный ливень
    82: "🌧",  # Сильный ливень
    95: "⛈",  # Гроза
    96: "⛈🌨", # Гроза с градом
    99: "⛈❄️" # Сильная гроза с градом
}

def get_weather_for_cities():
    result = []

    for city, coords in CITIES.items():
        params = {
            "latitude": coords["lat"],
            "longitude": coords["lon"],
            "current_weather": "true"
        }

        response = requests.get(API_URL, params=params, timeout=10)
        if response.status_code != 200:
            continue

        data = response.json()
        weather = data.get("current_weather")
        if not weather:
            continue

        code = weather.get("weathercode", 0)
        description = WEATHER_CODES.get(code, "Неизвестно")
        icon = WEATHER_ICONS.get(code, "")

        result.append({
            "city": city,
            "temperature": weather["temperature"],
            "wind": weather["windspeed"],
            "description": description,
            "icon": icon
        })

    return result
