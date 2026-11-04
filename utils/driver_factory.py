from selenium import webdriver


def create_driver(browser: str = "chrome", headless: bool = False):
    if browser.lower() != "chrome":
        raise ValueError(f"Unsupported browser: {browser}")

    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1440,1000")
    return webdriver.Chrome(options=options)
