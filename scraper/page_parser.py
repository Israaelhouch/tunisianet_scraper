import logging
from bs4 import BeautifulSoup
from scraper.utils.config import SITE_CONFIG

def scrape_page_from_html(html):
    soup = BeautifulSoup(html, "html.parser")
    products = []
    for product in soup.select(SITE_CONFIG["product_container"]):
        try:
            name = product.select_one(SITE_CONFIG["name"]).get_text(strip=True) if product.select_one(SITE_CONFIG["name"]) else ""
            price = product.select_one(SITE_CONFIG["price"]).get_text(strip=True) if product.select_one(SITE_CONFIG["price"]) else ""
            image = product.select_one(SITE_CONFIG["image"])["src"] if product.select_one(SITE_CONFIG["image"]) else ""
            availability_el = product.select_one(SITE_CONFIG["availability"])
            availability = availability_el.get_text(strip=True) if availability_el else "N/A"
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
