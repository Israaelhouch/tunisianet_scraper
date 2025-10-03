from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def init_driver(headless=True):
    options = Options()
    if headless:
        options.add_argument("--headless=new")  # Use modern headless mode
        options.add_argument("--disable-gpu")  # Prevent GPU use
        options.add_argument("--disable-software-rasterizer")  # Prevent software fallback
        options.add_argument("--disable-dev-shm-usage")  # Avoid shared memory issues
        options.add_argument("--no-sandbox")  # Needed in some environments
        options.add_argument("--disable-extensions")  # Disable Chrome extensions
        options.add_argument("--disable-background-networking")  # Prevent background connections
        options.add_argument("--disable-default-apps")
        options.add_argument("--disable-sync")
        options.add_argument("--disable-translate")
        options.add_argument("--metrics-recording-only")
        options.add_argument("--mute-audio")
        options.add_argument("--no-first-run")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-background-timer-throttling")
        options.add_argument("--disable-backgrounding-occluded-windows")
        options.add_argument("--disable-renderer-backgrounding")
        options.add_argument("--disable-features=TranslateUI,BlinkGenPropertyTrees")  # Disable unnecessary Chrome features

    # Force software rendering and disable GPU entirely
    options.add_argument("--use-gl=swiftshader")

    # Set window size
    options.add_argument("--window-size=1920,1200")

    return webdriver.Chrome(options=options)
