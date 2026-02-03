import os
from datetime import date
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("apod_key")
safe_date = date(2000, 1, 1)
SAVE_DIR = "your_dir_path"
url = "https://api.nasa.gov/planetary/apod"
