import time, logging, csv
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from scraper.utils.config import MAX_THREADS
from scraper.utils.driver import init_driver
from scraper.utils.categories_extraction import get_category_urls
from scraper.category_parser import scrape_category
from scraper.storage import save_to_csv, save_to_json

logging.basicConfig(filename="scraper.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    start_time = time.time()
    main_url = "https://www.tunisianet.com.tn/"
    driver = init_driver(headless=True)
    category_urls = get_category_urls(driver, main_url)
    driver.quit()

    csv_file = open("data/products.csv", "w", newline="", encoding="utf-8")
    writer = csv.writer(csv_file)
    writer.writerow(["name","price","image","availability","description","url","category"])

    all_products = []

    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        future_to_url = {executor.submit(scrape_category, init_driver, name, url): (name, url) for name, url in category_urls}
        for future in tqdm(as_completed(future_to_url), total=len(future_to_url), desc="Scraping categories"):
            name, url = future_to_url[future]
            try:
                products = future.result()
                logging.info(f"{len(products)} products scraped from {name}")
                save_to_csv(products, writer)
                save_to_json(products, "data/products.json")
                all_products.extend(products)
            except Exception as e:
                logging.error(f"Error scraping {name}: {e}")

    csv_file.close()
    logging.info(f"Scraping finished. Total products: {len(all_products)}")
    logging.info(f"Total time: {time.time()-start_time:.2f}s")

if __name__ == "__main__":
    main()
