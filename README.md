# 🐾 Zootopia Animal Info Generator

This project is a Python-based application that allows users to search for animal data using the [API Ninjas Animals API](https://api-ninjas.com/api/animals) and generates a styled HTML page with the results.

---

## 🚀 Features

- ✅ Search for any animal using a command-line interface.
- ✅ Retrieves live data such as taxonomy, habitat, diet, top speed, and lifespan.
- ✅ Uses a pre-built HTML template (`animals_template.html`) to render results dynamically.
- ✅ Generates an output file `animals.html` that you can open in any browser.
- ✅ Uses environment variables to safely manage API keys.

---

## 📂 Project Structure
├── animals_web_generator.py # Main application logic
├── data_fetcher.py # Handles the API request and data fetching
├── animals_template.html # HTML template with placeholders
├── animals.html # Auto-generated output file
├── .env # Stores your API key (not committed)
├── README.md # You're here!
└── requirements.txt # Dependencies list

## Install Dependencies
pip install -r requirements.txt

## 📂 Create .env File 
touch .env
Open .env and enter API_KEY=your_api_key_here


## 🚀 Run
python animals_web_generator.py
# Zootopia-with-API
