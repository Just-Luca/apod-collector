# APOD-Collector
APOD Collector (collector.py) is a Python script that downloads and archives images from NASA’s Astronomy Picture of the Day (APOD) using the official NASA API.  It allows you to fetch all APOD images over a configurable date range and save them locally.
By default, thanks to utils.get_start_date() function, it starts downloading images from your last saved one. If it's your FIRST download, it falls back to a "safe" date: constants.safe_date = date(2000, 1, 1). Of course you can manually modify the starting (and ending) date (e.g.: start_date = date(1995, 6, 16)).
