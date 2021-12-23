# 네이버 시가총액 순위 검색 -> 1~200등 기업 웹 스크래핑 목표!

# 네이버 증권을 Ctrl+Shift+C로 확인 결과 'table'형태로 구성됨 ex. thead = tablehead, tbody = tablebody 등
# -> table 정보를 불러온 후, thead, tbody, tr, td 등을 처리하면 됨 



import csv                                                         # 파이썬에 원래있는 csv 함수 불러오기
import requests
from bs4 import BeautifulSoup


url = "https://finance.naver.com/sise/sise_market_sum.nhn?&page="

filename = "시가총액 1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")           # 파일 저장 시 자동으로 한칸 띄어서 줄바꿈 저장을 함 -> newline=""으로 한캉 띄우기 삭제 가능
writer = csv.writer(f)                                              # 엑셀로 파일 불렀을 때 글자 깨지면 인코딩을 utf8 -> utf-8-sig로 변경하면 됨 

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
# 웹 페이지에서 긁어온 데이터 제목을 .split("\t")를 통해 탭으로 나눔
print(type(title))                                                  # title이 어떤 형태인지 확인 -> 리스트 -> 별도의 변환없이 .writerow 바로 사용 가능
writer.writerow(title)                                              # 해석 : 생성할 csv 파일에 title 값을 입력

for page in range(1,5):

    res = requests.get(url + str(page))                             # 반복문, range에 의해 page는 1, 2, 3,4 가 순차적으로 들어감
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    # html을 분석한 결과 thead, tbody 둘 다 tr 값 존재 -> tbody에서 필요한 데이터 추출
    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    # 해석 : 테이블 내 type_2 클래스를 불러온 후, tbody 내의 tr의 모든 값을 추출

    for row in data_rows:
        columns = row.find_all("td")                                # tbody 내 td 값 -> 행렬의 row 값들 -> 반복문을 통해 값 가져오기
 
        # 출력 결과, 공백, 줄바꿈 태그 등 까지 모두 출력 -> 확인 결과 줄바꿈을 위한 tr 태그 등이 존재 -> tr 내 td가 1개 이므로 공백을 continue로 스킵
        if len(columns) <= 1:                              
            continue

        data = [column.get_text().strip() for column in columns]    # 나도코딩 기본편 6-5 한줄 for 참조, .strip : 공백 제거 함수
        # print(data)
        writer.writerow(data)                                       # 변수.writerow() : 리스트 형태로 되어있는 데이터 변환 (?)
