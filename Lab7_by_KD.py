import requests


def get_weather(city_name, api_key):
    """
    Показывает погоду, влажность и давление в указанном городе
    """
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric', 
        'lang': 'ru'
    }
    
    try:
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()
        
        data = response.json()
        
        city = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        description = data['weather'][0]['description']
        
        
        print("\n" + "="*40)
        print(f"ПОГОДА В ГОРОДЕ {city.upper()}, {country}")
        print("="*40)
        print(f"Температура: {temp:.1f}°C")
        print(f"Влажность: {humidity}%")
        print(f"Давление: {pressure} гПа")
        print(f"Описание: {description.capitalize()}")
        print("="*40)
        
    except requests.exceptions.Timeout:
        print("Ошибка: Упс, Превышено время ожидания. Попробуйте снова.")
    except requests.exceptions.ConnectionError:
        print("Ошибка: Нет соединения с сервером.")
    except requests.exceptions.HTTPError as e:
        if response.status_code == 401:
            print("Ошибка: Неверный API ключ, братик")
        else:
            print(f"Ошибка HTTP: {e}")
    except Exception as e:
        print(f"Ошибка: {e}")


API_KEY = "75a16bc8a78bc52b91da5973bc6360a3"
CITY = "Rome"


get_weather(CITY, API_KEY)