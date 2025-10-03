# Web Scraping & Automation Project

## Project Overview
This Python-based project is designed for **web scraping and automation**. It extracts data from websites dynamically and efficiently, handling both static and JavaScript-rendered pages.

---

## Features
- Extract categories, subcategories, and item URLs from websites.
- Handle multi-page navigation and hover-based content.
- Supports static HTML parsing (**BeautifulSoup**) and dynamic scraping (**Selenium**).
- Saves data in structured formats: CSV or JSON.
- Implements logging and error handling for robust scraping.

---

## Technologies & Libraries
- **Python 3.x**
- **Selenium** – Browser automation for dynamic content.
- **BeautifulSoup** – HTML parsing.
- **WebDriverWait & ExpectedConditions** – Manage dynamic elements.
- **pandas** – Data storage and manipulation.
- **logging** – Track scraping process and errors.
- Optional: **MongoDB/SQL** – For structured data storage.

---

## Installation

```bash
git clone https://github.com/yourusername/project-name.git  # Clone the repository
cd tunisianet_scraper                                       # Navigate to the project folder
pip install -r requirements.txt                             # Install dependencies
python main.py                                              # pip install -r requirements.txt
```

---

## Project Structure

```markdown
project-name/
├── 📁 data
│   ├── 📁 __pycache__/ 🚫 (auto-hidden)
│   ├── 📁 utils/
│   │   ├── 📁 __pycache__/ 🚫 (auto-hidden)
│   │   ├── 🐍 categories_extraction.py
│   │   ├── 🐍 config.py
│   │   └── 🐍 driver.py
│   ├── 🐍 category_parser.py
│   ├── 🐍 page_parser.py
│   └── 🐍 storage.py
├── 🚫 .gitignore
├── 📖 Readme.md
├── 🐍 main.py
├── 📄 requirements.txt
└── 📋 scraper.log 🚫 (auto-hidden)
```