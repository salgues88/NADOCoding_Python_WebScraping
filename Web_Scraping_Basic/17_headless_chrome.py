# Headless Chrome

# 16_selenium_movies_scroll 에서 매번 화면을 띄우다 보니 속도느림 / 메모리 점유율 상승 등의 문제 발생

# 작업자가 서버 등에서 작업하고, 굳이 브라우저를 띄어서 확인하지 않아도 될 때 -> headless 라는 기능을 사용 (띄우지 않고 백그라운드에서 실행)



# headless 적용 방법
# options = webdriver.ChromeOptions()
# options.headless = True                                       # headless 적용
# options.add_argument("window-size=1920x1080")                 # 백그라운드 작동 윈도우 사이즈 지정

# browser = webdriver.Chrome(options=options) 





# 16_selenium_movies_scroll 파일 코드 복붙 및 주석 삭제 후 headless 관련 코드 추가


import time
from selenium import webdriver

from bs4 import BeautifulSoup



# webdriver.Chrome으로 불러오니 계속 에러표시가 떠서 에러표시 안나게 하는 방법 적용 (by 구글링)
options = webdriver.ChromeOptions()                                     

options.add_experimental_option("excludeSwitches", ["enable-logging"])

options.headless = True
options.add_argument("window-size=1920x1080")

browser = webdriver.Chrome(options=options) 

browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)


# 인터벌 함수 - 2초에 한번씩 스크린 내림 (time 함수)
interval = 2                                                                


# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")


# 스크롤 내리기 무한 반복 수행
while True:                                                                 # 무한 반복

    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 새로운 화면이 뜨는 시간동안 대기
    time.sleep(interval)

    # 업데이트 된 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:                                          
        break

    # 반복문이 수행되었으면 이전 높이를 현재 높이로 업데이트 함
    prev_height = curr_height


print("Selinium을 이용한 스크롤 내리기 완료")


# 백그라운드에서 돌아가는 화면을 확인하기 위한 스크린 샷 찍는 방법 (스크롤 맨 밑에 내려왔을 때 찍음)
browser.get_screenshot_as_file("google_movie_scroll_end.png")




# 기존 bs4, requests에서 selenium과 중복되는 부분 삭제 

soup = BeautifulSoup(browser.page_source, 'lxml')                       # res.text 대신 selenium의 browser를 불러오고, .page_source를 쓰면 됨




movies = soup.find_all("div", attrs={"class":"Vpfmgd"})  
print("영화 리스트 총 갯수 :", len(movies))                               # movies에 엘레멘트가 몇 개 있는지 확인용
print("\n")

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()

    # 할인 전 가격 
    original_price = movie.find("span", attrs={"class", "SUZt4c djCuy"})
    if original_price:                                                  
        original_price = original_price.get_text()
    else:                                                               
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