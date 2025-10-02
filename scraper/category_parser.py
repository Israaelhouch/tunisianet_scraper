import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from page_parser import scrape_page
from utils.config import SITE_CONFIG


def scrape_category(driver_init_func, category_name, category_url):


    driver = driver_init_func(headless=True)
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
            logging.warning(f"No products on page {page}: {category_url}")
            break

        products_page = scrape_page(driver.current_url)
        for p in products_page:
            p["category"] = category_name
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