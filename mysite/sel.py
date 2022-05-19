def login_facebook():
    from selenium import webdriver
    import time
    from selenium.webdriver.common.by import By

    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1366x768')
    chrome_options.add_argument('--allow-running-insecure-content')
    browser = webdriver.Chrome(options=chrome_options) #

    # try:
    #     browser.get("https://www.google.com")
    #     print(f"Page title was {browser.title}")

    # finally:
    #     browser.quit()

    browser.get("https://web.facebook.com/")

    time.sleep(2)

    user = '09059689401'
    userlog = browser.find_element(By.XPATH, '//*[@id="email"]')
    userlog.send_keys(user)

    password = 'combat@@fb'
    passwordlog = browser.find_element(By.XPATH, '//*[@id="pass"]')
    passwordlog.send_keys(password)

    # time.sleep(2)

    login = browser.find_element(By.NAME, 'login')
    login.click()

    time.sleep(2)

    name_text = browser.find_element(By.XPATH, '//span[@class="a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7"]')
    # name_text = browser.find_element(By.CSS_SELECTOR, 'span.a8c37x1j.ni8dbmo4.stjgntxs.l9j0dhe7')
    name = name_text

    # print(name)
    # print(name.get_attribute("innerHTML"))
    # print(name.text)
    # print("done")

    browser.quit()

    return name.text