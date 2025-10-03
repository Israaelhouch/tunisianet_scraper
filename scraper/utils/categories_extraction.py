
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_category_urls(driver, main_url):
    """
    Extract category names and URLs from the main page.
    Returns:
        list of tuples: (category_name, category_url)
    """
    logging.info(f"Opening main page: {main_url}")
    driver.get(main_url)
    driver.maximize_window()

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".item-line a"))
    )

    items = driver.find_elements(By.CSS_SELECTOR, ".item-line a")
    urls = []

    for item in items:
        href = item.get_attribute("href")
        text = item.text.strip()
        if not text:
            text = item.get_attribute("innerText").strip()

        if href:
            urls.append((text, href))

    logging.info(f"Found {len(urls)} categories on main page")
    return urls
 