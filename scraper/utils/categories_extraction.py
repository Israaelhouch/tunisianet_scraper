# category.py
import time, logging
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

def get_category_urls(driver, main_url):
    """
    Extract category names and URLs from the main page.
    Returns a list of tuples: (category_name, category_url)
    """
    driver.get(main_url)
    driver.maximize_window()
    time.sleep(2)
    items = driver.find_elements(By.CSS_SELECTOR, ".item-line a")
    urls = [(item.text.strip(), item.get_attribute("href")) for item in items if item.get_attribute("href")]
    logging.info(f"Found {len(urls)} categories on main page")
    return urls
