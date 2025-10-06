import logging
from bs4 import BeautifulSoup
from scraper.utils.config import SITE_CONFIG

def scrape_page_from_html(html):
    soup = BeautifulSoup(html, "html.parser")
    products = []

    BASE_SELECTOR = SITE_CONFIG.get("breadcrumb_item") 

    main_category = "N/A"
    main_category_el = soup.select_one(BASE_SELECTOR + ":nth-child(2) a")
    if not main_category_el:
        main_category_el = soup.select_one(BASE_SELECTOR + ":nth-child(2)")

    if main_category_el:
        main_category = main_category_el.get_text(strip=True)

    sub_category = "N/A"
    sub_category_el = soup.select_one(BASE_SELECTOR + ":nth-child(3) a")
    if not sub_category_el:
        sub_category_el = soup.select_one(BASE_SELECTOR + ":nth-child(3)")

    if sub_category_el:
        sub_category = sub_category_el.get_text(strip=True)
        
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
                "name": name, 
                "price": price, 
                "image": image,
                "availability": availability, 
                "description": description,
                "url": link,
                "main_category": main_category, 
                "sub_category": sub_category
            })

        except Exception as e:
            logging.warning(f"Skipped product: {e}")

    return products