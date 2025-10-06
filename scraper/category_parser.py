import logging
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from scraper.page_parser import scrape_page_from_html
from scraper.utils.config import SITE_CONFIG
from scraper.utils.driver import init_driver

def scrape_category(category_name, category_url):
    """
    Scrapes all products from a given category URL.
    Each thread initializes its own Selenium driver.
    """
    driver = init_driver(headless=True)
    driver.get(category_url)
    all_products = []
    page = 1

    while True:
        logging.info(f"Scraping {category_name} page {page}: {category_url}")
        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, SITE_CONFIG["product_container"]))
            )
        except:
            logging.warning(f"No products found on page {page}: {category_url}")
            break

        products_page = scrape_page_from_html(driver.page_source)

        all_products.extend(products_page)

        try:
            next_btn = driver.find_element(By.XPATH, SITE_CONFIG["next_page"])
            next_url = next_btn.get_attribute("href")
            if not next_url or next_url == driver.current_url:
                break
            driver.get(next_url)
            page += 1
            time.sleep(1)
        except:
            break

    driver.quit()
    return all_products