import os
from datetime import datetime, timedelta, date
import requests

# --- Configuration ---
# Insert your API key here. You can get one for free at https://api.nasa.gov/
API_KEY = "your_key"

# --- Get Start Date Function ---
safe_date = date(2000, 1, 1)

def get_start_date(dir_path):

    if not os.path.exists(dir_path):
        return safe_date
    
    date_ar = []
    for f in os.listdir(dir_path):
        if f.endswith(('.gif', '.png')):
            try:
                # Rimuove sia .gif che .png
                nome = f.replace('.gif', '').replace('.png', '')
                data = datetime.strptime(nome, '%Y-%m-%d')
                date_ar.append(data)
            except ValueError:
                continue

    if max(date_ar).date() == date.today():
        return max(date_ar)
    
    else:
        return max(date_ar) + timedelta(days=1) if date_ar else safe_date

# Folder where images will be saved
SAVE_DIR = "your_path"

# --- Date calculation ---
start_date = get_start_date(SAVE_DIR)
end_date = date.today()

# Format dates for the API
start_date_str = start_date.strftime('%Y-%m-%d')
end_date_str = end_date.strftime('%Y-%m-%d')

# --- API request preparation ---
url = "https://api.nasa.gov/planetary/apod"
params = {
    'api_key': API_KEY,
    'start_date': start_date_str,
    'end_date': end_date_str
}

print(f"Retrieving images from {start_date_str} to {end_date_str}...")

# --- Perform the API request ---
try:
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an exception for HTTP error responses

    # --- Process the JSON response ---
    data = response.json()

    # --- Create the save directory if it does not exist ---
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)
        print(f"Folder '{SAVE_DIR}' created.")

    # --- Download and save the images ---
    for record in data:
        if record.get('media_type') == 'image':
            image_url = record.get('url')
            image_date = record.get('date')
            file_name = f"{image_date}.gif"
            file_path = os.path.join(SAVE_DIR, file_name)

            print(f"Downloading: {file_name}")
            try:
                image_response = requests.get(image_url)
                image_response.raise_for_status()
                with open(file_path, 'wb') as f:
                    f.write(image_response.content)
            except requests.exceptions.RequestException as e:
                print(f"Unable to download image {image_url}: {e}")

    print("\nDownload completed.")

except requests.exceptions.RequestException as e:
    print(f"Error during API request: {e}")
except KeyError as e:
    print(f"Error while processing data: missing key {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
