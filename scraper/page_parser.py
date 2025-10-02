import time, logging, requests
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from scraper.utils.config import SITE_CONFIG, MAX_RETRIES

def scrape_page(url):
    for attempt in range(MAX_RETRIES):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code != 200:
                logging.warning(f"Failed {url} status code {response.status_code}")
                continue
            soup = BeautifulSoup(response.text, "html.parser")
            products = []
            for product in soup.select(SITE_CONFIG["product_container"]):
                try:
                    name = product.select_one(SITE_CONFIG["name"]).get_text(strip=True) if product.select_one(SITE_CONFIG["name"]) else ""
                    price = product.select_one(SITE_CONFIG["price"]).get_text(strip=True) if product.select_one(SITE_CONFIG["price"]) else ""
                    image = product.select_one(SITE_CONFIG["image"])["src"] if product.select_one(SITE_CONFIG["image"]) else ""
                    availability = product.select_one(SITE_CONFIG["availability"]).get_text(strip=True) if product.select_one(SITE_CONFIG["availability"]) else "N/A"
                    description = product.select_one(SITE_CONFIG["description"]).get_text(strip=True) if product.select_one(SITE_CONFIG["description"]) else ""
                    link = product.select_one(SITE_CONFIG["product_url"])["href"] if product.select_one(SITE_CONFIG["product_url"]) else ""
                    products.append({
                        "name": name, "price": price, "image": image,
                        "availability": availability, "description": description,
                        "url": link
                    })
                except Exception as e:
                    logging.warning(f"Skipped product: {e}")
            return products
        except Exception as e:
            logging.warning(f"Retry {attempt+1} failed for {url}: {e}")
    return []


