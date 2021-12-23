# Selenium 활용 2-2 (beautiful soup4와 requests, selenium을 모두 이용하여 구글 무비 인기순위 데이터 출력)

# selenium을 이용한 동적 페이지 웹 스크래핑 코드

import time
from selenium import webdriver

from bs4 import BeautifulSoup


# webdriver.Chrome으로 불러오니 계속 에러표시가 떠서 에러표시 안나게 하는 방법 적용 (by 구글링)
options = webdriver.ChromeOptions()                                     
options.add_experimental_option("excludeSwitches", ["enable-logging"])


browser = webdriver.Chrome(options=options) 


browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)


# 동적 페이지의 아래 항목을 보기 위해서는 스크롤을 아래로 내려야 함
# -> 지정한 위치(1080)로 스크롤 내리기      (해당 코딩은 자바스크립트 이용 (이해를 하지 않아도 됨)) 
# browser.execute_script("window.scrollTo(0, 1080)")                          # window.scrollTo(0, 1080) : To의 T는 대문자, (0, 1080) - 디스플레이 해상도


# 화면 가장 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")    # document.body.scrollHeight : 현재 화면 가장 아래로 스크롤 내리는 기능


# 인터벌 함수 - 2초에 한번씩 스크린 내림 (time 함수)
interval = 2                                                                


# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")


# 스크롤 내리기 무한 반복 및 끝까지 내린 후 자동 멈춤 코드
while True:                                                                 # 무한 반복

    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 새로운 화면이 뜨는 시간동안 대기
    time.sleep(interval)

    # 업데이트 된 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:                                          # 현재 스크롤 높이와, 이전 스크롤 높이가 같으면 더 업데이트 할께 없음 -> 탈출
        break
#                                                                             현재 스크롤 높이가 이전 스크롤 높이보다 더 높으면 -> 업데이트 됨 -> 스크롤 내리기 반복

    # 반복문이 수행되었으면 이전 높이를 현재 높이로 업데이트 함
    prev_height = curr_height


print("Selinium을 이용한 스크롤 내리기 완료")




# 기존 bs4, requests에서 selenium과 중복되는 부분 삭제 

soup = BeautifulSoup(browser.page_source, 'lxml')                       # res.text 대신 selenium의 browser를 불러오고, .page_source를 쓰면 됨


# (파일 정보 불러오기 중복 발생 케이스)
# movies = soup.find_all("div", attrs={"class":["ImZGtf mpg5gc", "Vpfmgd"]})  # 이름이 상이한 class를 불러올 땐 '리스트'로 묶어서 호출 가능!
# print(len(movies))                                                      # movies에 엘레멘트가 몇 개 있는지 확인용


# (위에서 div class 이름을 2개 불러 왔는데 처음 영화 10개 중복 발생 -> 확인 결과 "Vpfmgd" 하나만 있으면 됨)
movies = soup.find_all("div", attrs={"class":"Vpfmgd"}) 
print("영화 리스트 총 갯수 :", len(movies))                               # movies에 엘레멘트가 몇 개 있는지 확인용
print("\n")

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()

    # 할인 전 가격 
    original_price = movie.find("span", attrs={"class", "SUZt4c djCuy"})
    if original_price:                                                  # 해석 : 오리지날 가격 정보(div class="SUZt4c djCuy")가 있으면
        original_price = original_price.get_text()
    else:                                                               # 해석 : 오리지날 가격 정보(div class="SUZt4c djCuy")가 없으면 (할인 안하는 영화는 "SUZt4c djCuy" 값이 없음)
        print(title, "(할인되지 않은 영화는 제외)")
        print("-"*120)
        continue                                                         
    
    # 할인 된 가격
    price = movie.find("span", attrs={"class", "VfPpfd ZdBevf i5DZme"}).get_text()

    # 링크 정보
    link = movie.find("a", attrs={"class":"JC71ub"})["href"]      
    # 위 a hef의 링크는 "/store/movies/details/%EA%B3%A0%EC%A7%88%EB%9D%BC_VS_%EC%BD%A9?id=bKfIMqA5r6Q.P" 형태로 앞부분이 짤려 있음

    # 올바른 링크 : https://play.google.com/ + a href 링크
    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print("링크 :", "https://play.google.com" + link)
    print("-"*120)

browser.quit()