# Selenium 활용2-1 (beautiful soup4와 requests를 이용하여 구글 무비 인기순위 데이터 출력)

# 구글 무비 -> 인기차트에서 할인하고 있는 영화만 스크래핑



# import requests
# from bs4 import BeautifulSoup


# url = "https://play.google.com/store/movies/top"
# res = requests.get(url)
# res.raise_for_status
# soup = BeautifulSoup(res.text, 'lxml')


# movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})
# print(len(movies))                                                      # movies에 엘레멘트가 몇 개 있는지 확인

# # movies에 엘레멘트가 0개로 표시 -> html을 저장해서 확인 필요
# with open("movie.html", "w", encoding="utf8") as f:
#     # f.write(res.text)

#     # f.write(res.text)로 html 문서 만든 후 엘레멘트를 확인하니 보기 어려움 -> res.text 대신 soup.prettify로 html 생성
#     f.write(soup.prettify())                                            # 변수.prettify : html 문서를 예쁘게 출력하는 함수


# html 파일을 연 후 "크루엘라" 등으로 검색했는데 검색불가 -> html을 띄어보니 영어로 된 구글무비 사이트가 오픈됨 
# -> 구글무비 등 일부 사이트는 접속하는 사용자의 Header 정보를 통해 사용자의 국적에 따라 맞춤형 사이트를 띄어줌
# -> 헤더 및 유저 에이전트 내용을 추가하면 됨



#####################################################################################################################

# 헤더, 유저 에이전트 정보 추가한 코딩


import requests
from bs4 import BeautifulSoup


url = "https://play.google.com/store/movies/top"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36", 
    "Accept-Language":"ko-KR,ko"                                        # 언어를 한글로 고정해서 불러옴 (해당 언어가 없으면 기본 페이지를 불러옴)
}

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')


movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})
# print(len(movies))                                                      # movies에 엘레멘트가 몇 개 있는지 확인용

# with open("movie.html", "w", encoding="utf8") as f:                     # headers에 User-Agent와 Accept-Language 정보 추가한 후 기존 html 파일 삭제하고 새로 생성
#     f.write(soup.prettify())

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)


# 구글 무비 인기차트에서 보이는건 수십개인데, 받아온 정보는 10개만 표시
# -> 구글 무비는 스크롤을 내리면 그 때 새로운 페이지를 보여줌 (이런 형태의 웹페이지를 '동적 페이지' 라고 부름)
# -> beautiful soup4와 requests는 동적 페이지 내용을 모두 불러올 수 없음
# -> 동적 페이지는 selenium을 이용하여 불러와야 함