# selenium의 webdriver를 사용하기 위한 import
from selenium import webdriver
from selenium.webdriver.common.by import By

# selenium으로 키를 조작하기 위한 import
from selenium.webdriver.common.keys import Keys

# 페이지 로딩을 기다리는데에 사용할 time 모듈 import
import time


# 크롬드라이버 실행
driver = webdriver.Chrome()

#크롬 드라이버에 url 주소 넣고 실행
driver.get('https://shopping.naver.com/home')

#페이지 로딩시 까지 기다림
driver.implicitly_wait(10)

#검색창 클릭
driver.find_element(By.CSS_SELECTOR,"button._combineHeader_expansion_search_button_u3JIl").click()
# search = driver.find_element(By.CSS_SELECTOR, 'input._searchInput_search_input_1Vu9r ._searchInput_input_text_2Jhbj').click()
search = driver.find_element(By.ID, 'input_text')
search.click()
time.sleep(2)

# 검색어 입력 후 엔터
search.send_keys("아이폰 13")
search.send_keys(Keys.ENTER)

time.sleep(5)







