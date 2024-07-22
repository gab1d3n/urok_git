import os
import requests
import asyncio
import aiohttp
from bs4 import BeautifulSoup

def fetch_image_with_requests(url, filename):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"Картинка сохранена в файл: {filename}")
        else:
            print(f"Ошибка при загрузке картинки, статус код: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при загрузке картинки: {e}")

async def fetch_image_with_aiohttp(url, filename):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    image_data = await response.read()
                    with open(filename, 'wb') as f:
                        f.write(image_data)
                    print(f"Картинка сохранена в файл: {filename}")
                else:
                    print(f"Ошибка при загрузке картинки, статус код: {response.status}")
    except aiohttp.ClientError as e:
        print(f"Ошибка при загрузке картинки: {e}")

def get_weather_with_split():
    url = 'https://www.gismeteo.kz/weather-astana-5137/'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            html = response.text
            start_index = html.find('<span class="unit unit_temperature_c">') + len('<span class="unit unit_temperature_c">')
            end_index = html.find('</span>', start_index)
            weather = html[start_index:end_index]
            print(f"Погода в Астане (через string.split()): {weather}")
        else:
            print(f"Ошибка при запросе: статус код {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе: {e}")

def get_weather_with_bs4():
    url = 'https://www.gismeteo.kz/weather-astana-5137/'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            temperature_element = soup.find('span', class_='unit unit_temperature_c')
            if temperature_element:
                weather = temperature_element.text.strip()
                print(f"Погода в Астане (через BeautifulSoup): {weather}")
            else:
                print("Не удалось найти данные о погоде")
        else:
            print(f"Ошибка при запросе: статус код {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе: {e}")

async def main():
    image_urls = [
        'https://i0.wp.com/www.motorsportitalia.it/wp-content/uploads/2022/07/ferrari-1.jpg?fit=958%2C637&ssl=1',
        'https://i0.wp.com/www.motorsportitalia.it/wp-content/uploads/2022/07/ferrari-1.jpg?fit=958%2C637&ssl=1',         
        'https://i0.wp.com/www.motorsportitalia.it/wp-content/uploads/2022/07/ferrari-1.jpg?fit=958%2C637&ssl=1',
        'https://i0.wp.com/www.motorsportitalia.it/wp-content/uploads/2022/07/ferrari-1.jpg?fit=958%2C637&ssl=1',
        'https://i0.wp.com/www.motorsportitalia.it/wp-content/uploads/2022/07/ferrari-1.jpg?fit=958%2C637&ssl=1',
        'https://i0.wp.com/www.motorsportitalia.it/wp-content/uploads/2022/07/ferrari-1.jpg?fit=958%2C637&ssl=1',
        'https://i0.wp.com/www.motorsportitalia.it/wp-content/uploads/2022/07/ferrari-1.jpg?fit=958%2C637&ssl=1',
        'https://i0.wp.com/www.motorsportitalia.it/wp-content/uploads/2022/07/ferrari-1.jpg?fit=958%2C637&ssl=1',
        'https://i0.wp.com/www.motorsportitalia.it/wp-content/uploads/2022/07/ferrari-1.jpg?fit=958%2C637&ssl=1',
    ]
    output_dir_requests = 'random_images_requests'
    os.makedirs(output_dir_requests, exist_ok=True)

    for i, url in enumerate(image_urls):
        filename = os.path.join(output_dir_requests, f'image_{i+1}_requests.jpg')
        fetch_image_with_requests(url, filename)

    output_dir_aiohttp = 'random_images_aiohttp'
    os.makedirs(output_dir_aiohttp, exist_ok=True)

    tasks = []
    for i, url in enumerate(image_urls):
        filename = os.path.join(output_dir_aiohttp, f'image_{i+1}_aiohttp.jpg')
        task = fetch_image_with_aiohttp(url, filename)
        tasks.append(task)

    await asyncio.gather(*tasks)

    get_weather_with_split()

    get_weather_with_bs4()

if __name__ == "__main__":
    asyncio.run(main())
