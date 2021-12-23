# Selenium 활용1 (네이버 항공권)

from selenium import webdriver

# 다음 웹으로 이동 시 딜레이 시간이 많이 걸릴 때, 화면이 넘어간 후에 다음 동작을 실행할 수 있는 기능을 구현하는 selenium 내장함수 3종
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC        # 너무 길어서 EC로 재명명


options = webdriver.ChromeOptions()                                     # webdriver.Chrome으로 불러오니 계속 에러표시가 떠서 에러표시 안나게 하는 방법 적용 (by 구글링)
options.add_experimental_option("excludeSwitches", ["enable-logging"])

browser = webdriver.Chrome(options=options)   

browser.maximize_window()  # 창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url) # url 로 이동


# 가는날 선택 클릭
browser.find_element_by_link_text("가는날 선택").click()


# 다음달 27일, 다음달 28일 선택
# browser.find_elements_by_link_text("27")[1].click()                             # 26 요소가 여러개 -> find element's'로 검색하고, 리스트 위치 표시
# browser.find_elements_by_link_text("28")[1].click()


# 이번달 31일, 다음달 9일 선택
browser.find_elements_by_link_text("31")[0].click()
browser.find_elements_by_link_text("9")[1].click()


# 제주도 선택   (기존 링크주소 선택 시 not clickable at point 에러 발생 (포인트 클릭 불가능) -> 그 위 상위 태그 주소로 입력)
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()   # xpath 내에 큰 따옴표"" 가 이미 존재 -> 기존 큰 따옴표와 중복을 막기 위해 작은 따옴표''로 변경


# 항공권 검색
browser.find_element_by_link_text("항공권 검색").click()


# 검색 후 첫번째 결과 출력    
# elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]") 
# print(elem.text)
# (출력 결과 NoSuchElementException 에러 표시 -> 화면이 바로 안뜨고 딜레이 발생 -> 선택 에러 -> 실패))


# 검색 후 첫번째 결과 출력 수정
### 항권권 검색 시 딜레이 시간이 많이 걸림 -> 화면 넘어간 후에 다음 동작을 수행하도록 하는 함수를 사용해서 딜레이 구현 (class name, link text, xpath 등 다양하게 사용가능)
try:                # (성공했을 때는 동작 수행)
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]"))) 
    ### 위 코드 해석 : 브라우저가 최대 10초 동안 대기 until Xpath가 ""인 엘레멘트가 나올 때 까지 (이 때 (By.ZZZ, "")는 튜플 형태로 집어넣어야 함!!!)
    print(elem.text)# 첫번째 결과 출력

finally:            # (성공했을 때는 코딩한 동작 수행 후 종료, 실패했을 때는 바로 종료)
    browser.quit()


