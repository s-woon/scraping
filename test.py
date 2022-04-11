import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

player = []

driver = webdriver.Chrome("./chromedriver")  # 크롬드라이버 열기
driver.get("https://kr.ufc.com/rankings")  # 해당 url 접속
time.sleep(1)
driver.maximize_window()
time.sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

player_list = driver.find_elements(By.CSS_SELECTOR, "#block-mainpagecontent > div > div.l-container > div > div > div > div.view-content > div.view-grouping")
# print( '상품 개수: {}'.format(len(player_list)))
# print(player_list[0].get_attribute('innerHTML'))
for players in player_list:
    division = players.find_element(By.CSS_SELECTOR, 'div.view-grouping-content > table > caption > div > div.info > h4').text
    champion = players.find_element(By.CSS_SELECTOR, 'div.view-grouping-content > table > caption > div > div.info > h5 > div > div > div > a').text


    champion_info = {
        'Division': division,
        'ChampionName': champion,

    }
    player.append(champion_info)

print(player)