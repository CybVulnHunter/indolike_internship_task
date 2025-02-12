# 🌐 Web Page Link Extractor

## 📌 Overview
Web Page Link Extractor is a Python script that fetches a webpage's HTML content and extracts different types of links, such as JavaScript, PHP, and HTML files. This tool helps in analyzing web pages and collecting essential URLs. 🔍✨

## 🚀 Features
- 🌍 **Fetch HTML** - Retrieve webpage content with proper request handling.
- 🔗 **Extract Links** - Identify JavaScript, PHP, HTML, and other URLs.
- ✅ **Error Handling** - Handles connection errors, SSL verification, and timeouts.
- 🔄 **Automatic URL Formatting** - Converts relative links to absolute links.

## 📦 Requirements
- 🐍 Python 3.x
- 📦 `requests`
- 📦 `beautifulsoup4`

## ⚙️ Installation
Clone the repository using the following command:
```sh
🚀 git clone https://github.com/CybVulnHunter/indolike_internship_task.git
📂 cd indolike_internship_task
```
Install dependencies:
```sh
pip install -r requirements.txt
```

## ▶️ Usage
Run the script using Python:
```sh
🖥️ python web_scraper.py
```
Modify the script to input your desired URL for analysis.

## 🛠️ How It Works
1️⃣ **Fetch HTML** - The script requests a webpage and retrieves its HTML content.
2️⃣ **Parse Content** - BeautifulSoup is used to analyze the HTML structure.
3️⃣ **Extract Links** - Links are categorized as JavaScript, PHP, HTML, or other URLs.
4️⃣ **Display Results** - The extracted links are printed or stored for further use.

