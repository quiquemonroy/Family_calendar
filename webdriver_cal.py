from selenium import webdriver


def show_cal():
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:8000")
    # exit()
    # driver.close()


if __name__ == "__main__":
    show_cal()
