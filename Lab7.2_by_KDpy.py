import requests

def get_holidays(api_key, country, year):
    """
    Получает и выводит праздники для указанной страны
    """
    url = "https://holidayapi.com/v1/holidays"
    
    params = {
        'key': api_key,
        'country': country,
        'year': year
    }
    
    try:
        response = requests.get(url, params=params, timeout=30)
        data = response.json()
        
        if 'error' in data:
            print(f"Ошибка: {data['error']}")
            return
        
        holidays = data.get('holidays', [])
        
        if not holidays:
            print("Праздники не найдены")
            return
        

        print(f"\nПРАЗДНИКИ В СТРАНЕ {country} НА {year} ГОД")
        print("-" * 50)
        print(f"Всего найдено: {len(holidays)} праздников\n")
        
        for i, holiday in enumerate(holidays[:7], 1):
            name = holiday['name']
            date = holiday['date'][:10]  
            public = "Да" if holiday.get('public') else "Нет"
            
            print(f"{i}. {name}")
            print(f"   Дата: {date}")
            print(f"   Государственный: {public}")
            print()
            
    except requests.exceptions.RequestException as e:
        print(f"Ошибка соединения: {e}")

# Входные данные
API_KEY = "645a79f7-1d35-494b-a0eb-0c1bf439018e"  
COUNTRY = "RU"  
YEAR = 2025     

# Запуск
get_holidays(API_KEY, COUNTRY, YEAR)