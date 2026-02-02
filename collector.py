import os
import datetime
import requests

# --- Configuration ---
# Insert your API key here. You can get one for free at https://api.nasa.gov/
API_KEY = "DEMO_KEY"
# Folder where images will be saved
SAVE_DIR = "nasa_apod_images"

# --- Date calculation ---
years = 5
end_date = datetime.date.today()
start_date = end_date - datetime.timedelta(days=years * 365)

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
            image_title = record.get('title').replace(" ", "_").replace("/", "_")
            image_date = record.get('date')
            file_name = f"{image_date}_{image_title}.jpg"
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
