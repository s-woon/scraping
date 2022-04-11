import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

products = []

def search(key):

    driver = webdriver.Chrome("./chromedriver")  # 크롬드라이버 열기
    driver.get("https://trade.sa.nexon.com/")  # 해당 url 접속
    time.sleep(1)
    elem = driver.find_element(By.CLASS_NAME, "toggle-search")  # 검색버튼 찾기
    elem.click()  # 검색버튼 클릭
    elem = driver.find_element(By.ID, "txt_search")  # 입력창 찾기
    elem.click()  # 입력창 클릭
    elem.send_keys(f'{key}')  # 검색어 입력
    elem.send_keys(Keys.RETURN)  # 엔터키 입력
    time.sleep(1)  # 페이지 읽어들이는동안 대기

    # 맨 밑에까지 스크롤
    SCROLL_PAUSE_TIME = 0.5 # 스크롤하고 다음스크롤까지 대기시간
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    products_list = driver.find_elements(By.CSS_SELECTOR, "#ul_list > li") # 상품 목록이 담긴 li 담기
    print( '상품 개수: {}'.format(len(products_list))) # 상품 개수 출력
    print(products_list[0].get_attribute('innerHTML')) # 탐색한 요소의 HTML 태그 출력
    for product in products_list: # li에서 한개씩 꺼내서 딕셔너리로 저장
        prd_name = product.find_element(By.CSS_SELECTOR, 'div > div.title > b').text
        prd_count = product.find_element(By.CSS_SELECTOR, 'div.information > div:nth-child(1) > span.right > span.sl_count').text
        prd_price = product.find_element(By.CSS_SELECTOR, 'div.information > div:nth-child(2) > span.right.price > span').text
        product_info = {
            'name': prd_name,
            'count': prd_count,
            'price': prd_price
        }
        products.append(product_info)

    df = pd.DataFrame(products)
    print(df)
    df.to_csv('products_list.csv', index=False, encoding='utf-8-sig')

if __name__ == '__main__':
    print('ex) ak47, TRG21, marble, noble, g18 ... ')
    search(input('검색하실 아이템을 입력해주세요 : '))