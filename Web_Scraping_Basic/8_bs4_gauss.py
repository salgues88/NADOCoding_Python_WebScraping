# beautiful soup4 활용 1 가우스 전자


# beautiful soup로 출력 시 사용하는 함수 정리

### print(soup.title)                                           # 출력 후 네이버웹툰 홈피에서 개발자모드 진입 후 타이틀 확인 -> 동일함
### print(soup.title.get_text())                                # 타이틀 글자를 출력창에 표시
### print(soup.a)                                               # soup 객채 내 html 정보 중 첫번째 a 태그(=엘레멘트) 정보 출력
### print(soup.a.attrs)                                         # 객체.태그.attrs : a 태그의 속성(attrs) 정보를 딕셔너리로 출력
### print(soup.a["href"])                                       # 객체.태그[어떤 속성 정보] : a 태그 어떤 속성의 속성'값' 정보 출력




import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=675554"

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# 가우스 전자 시즌 3~4에서 Ctrl+Shift+C 눌린 후 에피소드 제목 클릭 -> 개발자 모드에서 코드값 확인
cartoons = soup.find_all("td", attrs={"class":"title"})     # .fild_all로 수집되는 정보는 '리스트 형태'로 반환됨

# title = cartoons[0].a.get_text()                            # <td class = "title"> 밑에 <a hef ~~>휴기 + 10년 후 가우스</a> 가 있음
# print(title)                                                # -> td 리스트 0번째의, a 태그의 제목을 출력

# link = cartoons[0].a["href"]
# print(link)                                                 # 원본 코드에 링크 앞부분이 잘려 있음 -> 인위적 보완 필요
# print("https://comic.naver.com" + link)



# 반복문을 이용하여 가우스전자 현재 페이지에 있는 제목과 주소 정리
for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = "https://comic.naver.com" + cartoon.a["href"]
    print(title, link)



print("\n줄 바꿈\n")
# 가우스전자 현재 페이지에 있는 에피소드 평균점수 구하기
# -> 점수에 Ctrl+Shift+C 상태에서 눌린 후 개발자모드 코딩 분석 -> 태그 : div, 클래스 : rating_type

total_rates = 0
cartoons2 = soup.find_all("div", attrs={"class":"rating_type"})
for cartoon2 in cartoons2:
    rate = cartoon2.find("strong").get_text()
    # print(rate)
    total_rates += float(rate)                              # float : 소수점을 포함하는 실수 (int : 정수) <- 평점이 문자열이라 계산을 위해 타입 변경 필요

total_rates = round(total_rates, 2)
print("전체 점수 :", total_rates)

avg_rates = round((total_rates / len(cartoons2)), 2)
print("평균 점수 :", avg_rates)



# vscode tip
# terminal 창에 python 이라고 검색하면 코드를 바로 입력 가능하고 결과를 볼 수 있음
# terminal 창에서 python을 끄고 싶으면 exit() 라고 입력하면 됨