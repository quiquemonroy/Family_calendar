from selenium import webdriver
import datetime

def show_cal():
    now = datetime.datetime.now()
    options = webdriver.FirefoxOptions()
    options.add_argument("-headless")
    options.binary_location = "/snap/firefox/current/usr/lib/firefox/firefox"
    options.add_argument("--width=800")
    options.add_argument("--height=480")
    driver = webdriver.Firefox(options=options)
    driver.get("http://127.0.0.1:8000")
    driver.save_full_page_screenshot(f"static/capturas/{now.now()}.png")
    # exit()
    driver.quit()


if __name__ == "__main__":
    show_cal()
