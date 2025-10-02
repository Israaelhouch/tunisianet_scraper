from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def init_driver(headless=True):
    options = Options()
    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-software-rasterizer")
    options.add_argument("--window-size=1920,1200")
    return webdriver.Chrome(options=options)