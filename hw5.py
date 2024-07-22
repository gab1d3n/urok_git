import os
import aiohttp
import json

async def fetch_json(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    print(f"Failed to fetch JSON, status code: {response.status}")
                    return None
    except aiohttp.ClientError as e:
        print(f"Error fetching JSON: {e}")
        return None

def save_json_to_file(json_data, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)
        print(f"JSON сохранен в файл: {filename}")
    except IOError as e:
        print(f"Error saving JSON to file: {e}")

async def main():
    url = 'https://jsonplaceholder.typicode.com/posts'

    json_data = await fetch_json(url)
    if json_data:
        output_dir = 'json_data_aiohttp'
        os.makedirs(output_dir, exist_ok=True)
        
        for obj in json_data:
            filename = os.path.join(output_dir, f'post_{obj["id"]}.json')
            save_json_to_file(obj, filename)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
