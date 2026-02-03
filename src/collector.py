import constants as cnts
from datetime import date
from utils import get_start_date, api_request_and_download

# First time? Maybe you want to start downloading from the very first APOD:
# start_date = date(1995, 6, 16)

start_date = get_start_date(cnts.SAVE_DIR)
end_date = date.today()

# Date formatting for the API
start_date_str = start_date.strftime('%Y-%m-%d')
end_date_str = end_date.strftime('%Y-%m-%d')

# --- Preparing the API request ---
params = {
    'api_key': cnts.API_KEY,
    'start_date': start_date_str,
    'end_date': end_date_str
}

api_request_and_download(params, cnts.SAVE_DIR)
