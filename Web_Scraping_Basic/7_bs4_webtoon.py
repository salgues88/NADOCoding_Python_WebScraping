import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# beautifulsoup4 
### find     : 조건에 해당하는 첫번째 태그 1개를 찾는 기능
### find_all : 조건에 해당하는 모든 태그를 가져오는 기능


# 네이버 웹툰 전체목록 가져오기 : 네이버 웹툰 홈페이지에서 요일별 전체 웹툰 밑 화요 웹툰을 Ctrl+Shift+C로 클릭해서 개발자 모드 위치 확인 
cartoons = soup.find_all("a", attrs={"class":"title"})       # 태그 이름 : a, 클래스 이름 : title인 모든 값을 가져옴


# 클래스 속성이 title인 모든 a 태그(=엘레멘트)를 반환
for cartoon in cartoons:
    print(cartoon.get_text())         



