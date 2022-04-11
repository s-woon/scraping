import urllib

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def search(key):
    chrome_options = webdriver.ChromeOptions() # 크롬드라이버 열기
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get("https://google.com/")  # 해당 url 접속
    time.sleep(1)
    elem = driver.find_element(By.NAME, "q")
    elem.send_keys(f'{key}')
    elem.send_keys(Keys.RETURN)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "#hdtb-msb > div:nth-child(1) > div > div:nth-child(2) > a").click()
    time.sleep(1)

    SCROLL_PAUSE_TIME = 1
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                driver.find_element(By.CSS_SELECTOR, ".mye4qd").click()
            except:
                break
        last_height = new_height

    images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")

    count = 1
    for image in images:
        try:
            image.click()
            time.sleep(2)
            imgUrl = driver.find_element(By.CSS_SELECTOR,
                '#Sva75c > div > div > div.pxAole > div.tvh9oe.BIB1wf > c-wiz > div > div.OUZ5W > div.zjoqD > div.qdnLaf.isv-id > div > a > img').get_attribute(
                "src")
            # opener = urllib.request.build_opener()
            # opener.addheaders = [('User-Agent',
            #                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
            # urllib.request.install_opener(opener)
            urllib.request.urlretrieve(imgUrl, str(count) + ".jpg")
            count = count + 1
        except:
            pass

if __name__ == '__main__':
    print('ex) 스폰지밥, 스폰지 ')
    search(input('다운받을 사진을 입력해주세요 : '))