# 🌤️ Desktop Weather Notifier Bot

A lightweight Python background script that fetches real-time weather metrics from the Open-Meteo API and triggers native desktop notifications.

## Features
- Fetches live temperature and weather condition codes based on geographic coordinates.
- Interprets raw WMO weather codes into readable status descriptions (Sunny, Cloudy, Rain).
- Displays native OS desktop popups using `plyer`.

## Tech Stack
- **Language:** Python 3
- **Libraries:** `requests` (HTTP requests), `plyer` (OS notifications)
- **API:** Open-Meteo REST API

## How to Run Locally

1. Clone this repository:
   ```bash
   git clone [https://github.com/Kurt-Amboy/weather-desktop-notifier.git](https://github.com/Kurt-Amboy/weather-desktop-notifier.git)
   cd weather-desktop-notifier
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python weather_bot.py
   ```# weather-desktop-notifier
