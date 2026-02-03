# 🌌 APOD-Collector

![GitHub repo size](https://img.shields.io/github/repo-size/Just-Luca/APOD-Collector) 
![GitHub contributors](https://img.shields.io/github/contributors/Just-Luca/APOD-Collector) 
![GitHub stars](https://img.shields.io/github/stars/Just-Luca/APOD-Collector?style=social) 
![GitHub license](https://img.shields.io/github/license/Just-Luca/APOD-Collector) 


**APOD Collector** (`src/collector.py`) is a Python script that downloads and archives images from NASA’s [Astronomy Picture of the Day (APOD)](https://apod.nasa.gov/apod/astropix.html) using the official NASA API. It fetches all APOD images over a configurable date range and saves them locally.  

By default, the script automatically resumes from the last saved image using `utils.get_start_date()`. If it’s your first download, it safely starts from `constants.safe_date = date(2000, 1, 1)`. You can also manually specify the starting (and ending) date, e.g.:  

```python
start_date = date(1995, 6, 16)
```

## ⚡ Features

![Features](https://img.shields.io/badge/Features-4-brightgreen)

- ✅ Download APOD images automatically via NASA API  
- ✅ Resume downloads from last saved image  
- ✅ Configurable date ranges  
- ✅ Organizes images locally with consistent naming
  

## 🛠 Installation & Dependencies

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)

Make sure you have **Python 3.7+** installed. Then, install dependencies with:

```bash
pip install -r requirements.txt
```

## 🔑 Usage

![Usage](https://img.shields.io/badge/Usage-Easy-brightgreen)

1. Get your free NASA API key from [https://api.nasa.gov/](https://api.nasa.gov/)  
2. Store it in a `.env` file:

```env
apod_key = your_personal_key
```

## 🚀 Contributing

![Contribute](https://img.shields.io/badge/Contributions-Welcome-brightgreen)

Contributions, issues, and feature requests are welcome!

1. Fork the repository  
2. Create your feature branch (`git checkout -b feature/MyFeature`)  
3. Commit your changes (`git commit -m 'Add some feature'`)  
4. Push to the branch (`git push origin feature/MyFeature`)  
5. Open a Pull Request  



