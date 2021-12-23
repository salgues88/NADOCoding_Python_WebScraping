# Beautiful Soup4 활용2(쿠팡)

# 쿠팡에서 급하게 코딩용 노트북을 구매해야할 때 리뷰 많고 평점 높은 노트북, 광고 붙은건 제외 등등


# 앞에서 배운 requests, re, user_agent, bs4 모두 활용해야 웹 스크래핑 가능



import requests
import re
from bs4 import BeautifulSoup



headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
# 헤더값 변경 없이 접속하니 쿠팡에서 거부당함 -> 사람이 접속하는 것처럼 user agent값을 입력함


for i in range(1, 6):                                                          # 쿠팡 노트북 검색 1~5 페이지 데이터 추출 -> 반복문 사용

    print("\n페이지 수 :", i)

    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={0}&rocketAll=false&searchIndexingToken=1=5&backgroundColor=".format(i)

    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    # print(res.text)                                                          # 쿠팡 -> 노트북으로 검색한 페이지의 정보가 잘 출력되는지 확인

    items = soup.find_all("li", attrs={"class":re.compile("^search-product")}) # re.compile() : 정규식
    # 해석 : li 태그 내 클래스가 search-product로 시작하는 모든 값을 가져옴


    for idx, item in enumerate(items):                                      # 응용 : 웹 스크래핑 결과를 txt 파일로 저장하기 위해 enumerate를 활용 -> 인덱스 번호 추가
        
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
            rate_cnt = rate_cnt.get_text()[1:-1]                            # 평점수 문자값 추출 : (20) 형태로 나옴 -> 슬라이싱을 통해 숫자 추출

        else:
            rate_cnt = "평점 수 없음"
            print("< 평점 수 없는 상품은 제외합니다 >")
            continue

        # 제품 링크
        link = item.find("a", attrs={"class":"search-product-link"})["href"] # 해석 : s-p-l 클래스의 a 정보를 찾고 href의 값을 가져오기

        # 평점 4.5점 이상, 평점수(=리뷰) 100개 이상만 표시
        if float(rate) >= 4.5 and float(rate_cnt) >= 100:
            # print(name, price, rate, rate_cnt)
            print(f"제품 이름 : {name}")                                    # f 문자열 (파이썬 기초편 4-4 문자열 포맷 참조)
            print(f"제품 가격 : {price}")
            print(f"제품 평점 : {rate} ({rate_cnt} 개)")
            print("바로가기 : {}".format("https://www.coupang.com" + link)) 
            print("-"*100)                                                 # 줄긋기 
        

        # 응용 : 반복문의 결과를 저장하기 위해 반복문에 enumerate 추가, 인덱스 번호를 with 저장문으로 사용
        with open("item{}.txt".format(idx + 1), "w", encoding="utf8") as f:        
            f.write(item.text)                                             # 문자 저장 시 .text, 이미지 저장 시 .content

