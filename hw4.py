import os
import requests
import json

def fetch_json(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching JSON: {e}")
        return None

def save_json_to_file(json_data, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)
        print(f"JSON сохранен в файл: {filename}")
    except IOError as e:
        print(f"Error saving JSON to file: {e}")

def main():
    url = 'https://jsonplaceholder.typicode.com/posts'

    json_data = fetch_json(url)
    if json_data:
        output_dir = 'json_data'
        os.makedirs(output_dir, exist_ok=True)
        
        for obj in json_data:
            filename = os.path.join(output_dir, f'post_{obj["id"]}.json')
            save_json_to_file(obj, filename)

if __name__ == "__main__":
    main()
