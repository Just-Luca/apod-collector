import os
import constants as cnts
import requests

from datetime import datetime, timedelta, date

def get_start_date(dir_path):

    if not os.path.exists(dir_path):
        return cnts.safe_date
    
    date_ar = []
    for f in os.listdir(dir_path):
        if f.endswith(('.gif', '.png')):
            try:
                nome = f.replace('.gif', '').replace('.png', '')
                data = datetime.strptime(nome, '%Y-%m-%d')
                date_ar.append(data)
            except ValueError:
                continue

    if max(date_ar).date() == date.today():
        return max(date_ar)
    
    else:
        return max(date_ar) + timedelta(days=1) if date_ar else cnts.safe_date
    
    
def api_request_and_download(params, save_dir):

    print(f"Retrieving images from {params['start_date']} to {params['end_date']}...")

    # --- Make the API request ---
    try:
        response = requests.get(cnts.url, params=params)
        response.raise_for_status()  # Check for HTTP errors

        # --- Process the JSON response ---
        data = response.json()

        # --- Create the save folder if it doesn't exist ---
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
            print(f"Folder '{save_dir}' created.")

        # --- Download and save images ---
        for record in data:
            if record.get('media_type') == 'image':
                image_url = record.get('url')
                image_date = record.get('date')
                file_name = f"{image_date}.gif"
                file_path = os.path.join(save_dir, file_name)

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
        print(f"Error during the API request: {e}")
    except KeyError as e:
        print(f"Error processing: missing key {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
