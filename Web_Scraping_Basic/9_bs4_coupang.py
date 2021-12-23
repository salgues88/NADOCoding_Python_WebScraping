# Beautiful Soup4 활용2(쿠팡)

# 쿠팡에서 급하게 코딩용 노트북을 구매해야할 때 리뷰 많고 평점 높은 노트북, 광고 붙은건 제외 등등


# 쿠팡에서 웹 스크레핑을 하기 위한 보충 설명
# HTTP Methond
### GET 방식 : 누구나 볼 수 있게 URL에 적어서 보내는 방식 (전송량 제한 -> 큰 데이터는 보낼 수 없음)
###            ex. http://www.coupang.com/np/search?minPrice=1000&maxPrice=100000&page=1 (? 뒤에 정보 표시, &로 구분)
### POST방식 : URL이 아닌 HTTP Body에 숨겨서 보내는 방식 (ID, PW 같은 보안 데이터는 숨겨서 보내야 함 -> POST)
###            ex. (나도코딩에서 예시 없음)


# 쿠팡의 경우 GET 방식 -> 쉽게 웹 스크래핑 가능!

# 앞에서 배운 requests, re, user_agent, bs4 모두 활용해야 웹 스크래핑 가능


import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"     # 쿠팡 노트북 검색 1page 링크 주소

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
# 헤더값 변경 없이 접속하니 쿠팡에서 거부당함 -> 사람이 접속하는 것처럼 user agent값을 입력함

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
# print(res.text)                                                          # 쿠팡 -> 노트북으로 검색한 페이지의 정보가 잘 출력되는지 확인

items = soup.find_all("li", attrs={"class":re.compile("^search-product")}) # re.compile() : 정규식
# 해석 : li 태그 내 클래스가 search-product로 시작하는 모든 값을 가져옴

# print(items[0].find("div", attrs={"class":"name"}).get_text())

# 헤더 없이 run 결과 '현재 연결은 사용자의 호스트 시스템의 소프트웨어의 의해 중단되었습니다' 라고 뜸 
# -> 봇이 접속하는걸 인지했는지 쿠팡에서 차단 -> User Agent 값을 바꿔서 사람이 접속하는 것처럼 시도할 필요가 있음
# -> header 변수 추가 및 user_agent 변경 후 res 변수에 headers=headers를 추가하니 추출 성공



for item in items:

    # 광고 제품 제외
    ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
    if ad_badge:
        print("< 광고 상품은 제외합니다>")
        continue                                                        # continue: 일종의 skip 기능 (밑의 문장 실행 X)

    # 제품 이름
    name = item.find("div", attrs={"class":"name"}).get_text()

    ### 애플 제품은 제외
    if "Apple" in name:                                                 # 해석 : name 변수 안에 Apple 이라는 문자열이 있으면
        print("< Apple 제품은 제외합니다 >")
        continue

    # 제품 가격
    price = item.find("strong", attrs={"class":"price-value"}).get_text()

    # 제품 평점
    rate = item.find("em", attrs={"class":"rating"})                    # rate(평점)은 없는 경우도 존재함
    if rate:
        rate = rate.get_text()
    else:
        rate = "평점 없음"
        print("< 평점 없는 상품은 제외합니다 >")
        continue                                                        # 평점, 평점수 없는건 continue 로 스킵하는 기능 추가
        
    # 제품 평점수 (=리뷰수)
    rate_cnt = item.find("span", attrs={"class":"rating-total-count"})  # 평점이 없음 -> 평점수도 없음
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()                                  # 평점수 문자값 : (20) 형태로 나옴 -> 슬라이싱으로 숫자만 추출 필요
        rate_cnt = rate_cnt[1:-1]                                       # 나도코딩 기본편 4-2 슬라이싱 참조
        # print("평점수 :", rate_cnt)                                   
    else:
        rate_cnt = "평점 수 없음"
        print("< 평점 수 없는 상품은 제외합니다 >")
        continue

    # 평점 4.5점 이상, 평점수(=리뷰) 100개 이상만 표시
    if float(rate) >= 4.5 and float(rate_cnt) >= 100:
        print(name, price, rate, rate_cnt)


    



