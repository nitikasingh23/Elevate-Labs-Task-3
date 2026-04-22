# Elevate-Labs-Task-3

# 📰 Web Scraper for News Headlines

## 📌 Objective
This project is a Python-based web scraper that extracts top headlines from a news website and saves them into a `.txt` file.

---

## 🛠 Tools & Libraries Used
- Python
- requests
- BeautifulSoup (bs4)

---

## ⚙️ How It Works

1. Sends an HTTP request to the news website using `requests`.
2. Parses the HTML content using `BeautifulSoup`.
3. Extracts headlines from `<h2>` tags.
4. Stores the headlines in a list.
5. Writes them into a file named `headlines.txt`.

---

## ▶️ How to Run

### 1. Install dependencies
pip install requests beautifulsoup4

### 2. Run the script
python scraper.py

### 3. Output
A file named `headlines.txt` will be created with all the headlines.

---

## 📌 Notes
- Website structure may change, so tags may need updates.
- This project is for learning purposes only.
