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
git clone https://github.com/yourusername/project-name.git  #1. Clone the repository:
cd tunisianet_scraper                                       #2. Navigate to the project folder
pip install -r requirements.txt                             #3. Install dependencies
python main.py                                              #4. pip install -r requirements.txt
```

---

## Project Structure
Describe your files so others know what each does:  

```markdown
project-name/
│
├─ main.py             # Main script to start scraping
├─ category.py         # Extract category URLs
├─ scraper.py          # Core scraping logic
├─ utils.py            # Helper functions (logging, saving data)
├─ requirements.txt    # Python dependencies
├─ data/               # Folder for scraped data
└─ README.md           # Project documentation
