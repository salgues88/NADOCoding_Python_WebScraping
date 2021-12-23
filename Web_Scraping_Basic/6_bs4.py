# Beautifulsoup4

# Beautiful Soup4 : Requests and/or Selenium으로 가져온 웹페이지 데이터 중 원하는 데이터를 추출하는 라이브러리 (웹 스크래핑)



# Beautiful Soup
# - Requests and/or Selenium으로 가져온 웹페이지 데이터 중 
#   원하는 데이터를 추출하는 라이브러리 (웹 스크래핑)

# - .find                     : 조건에 맞는 첫번째 element 출력
# - .find_all                 : 조건에 맞는 모든 element를 리스트로 찾아서 출력
# - .find_next_sibling(s)     : 다음 형제 찾기
# - .find_previous_sibling(s) : 이전 형제 찾기

# - soup["href"]              : 속성 (보통 a hef = 링크주소 형태로 많이 사용)
# - soup.get_text             : 텍스트



# pip install beautifulsoup4                                

# lxml : beautifulsoup4 기본 parser(파서) 라이브러리 (설치 후에는 import로 안불러 와도 됨)

# pip install lxml                                          



# import 모듈 vs from 모듈 import 메소드 / 변수 차이

### 1) import 모듈→ 해당 모듈 전체를 가져옴, 사용하려면 항상 '모듈명.메소드' 와 같이 모듈명을 앞에 붙여주어야 한다.

### 2) from 모듈 import 메소드 / 변수 → 해당 모듈 내에 있는 특정 메소드나 모듈 내 정의된 변수를 가져옴,
###    가져온 메소드나 변수를 앞에 모듈명을 붙이지 않고 그대로 사용할 수 있음 (다만, 이름이 같은 변수나 메소드가 존재할 경우 대체됨)

### 3) from 모듈 import * 이라고 하면 import 모듈과 동일하다. (사용 시 모듈명 붙이는 것 빼고)



import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")                      # 우리가 가져온 html 개체를 lxml 파서를 통해 beautifulsoup 객체로 변환
                                                            # (soup 객체는 html의 모든 정보를 가지고 있음!)


# 네이버 웹툰 홈페이지 -> Ctrl+Shift+C 눌린 상태에서 '웹툰 올리기' 버튼 클릭 후 개발자모드 내용을 아래에 표시

# <div class="asideButton upload">
#    <a href="/mypage/myActivity" class="Nbtn_upload" onclick="nclk_v2(event,'olk.upload');">웹툰 올리기</a>
# </div>

# 위에서 div, a : 태그(= 엘레멘트)   <- 태그는 <div> ~~ </div> 처럼 열림 / 닫힘을 둘 다 적어야 함
# 위에서 href : 속성                <- 속성은 </~~> 로 닫힘을 적을 필요 없음



# print(soup.title)                                           # 출력 후 네이버웹툰 홈피에서 개발자모드 진입 후 타이틀 확인 -> 동일함
# print(soup.title.get_text())                                # .get_text() : 글자를 가져와서 출력창에 표시
# print(soup.a)                                               # soup 객채 내 html 정보 중 첫번째 a 태그(=엘레멘트) 정보 출력
# print(soup.a.attrs)                                         # 객체.태그.attrs : a 태그의 속성(attrs) 정보를 딕셔너리로 출력
# print(soup.a["href"])                                       # 객체.태그[어떤 속성 정보] : a 태그 어떤 속성의 속성'값' 정보 출력

# (위 방법은 html 코드에 대한 이해가 높을 때 사용하는 방법 (일반적으로는 잘 모르기 때문에 find를 사용))


# print(soup.find("a", attrs={"class":"Nbtn_upload"}))        # Nbtn_upload는 홈피 개발자모드에서 Ctrl+Shift+C 눌린 후 내가 보고픈 화면에 커서를 올리면 확인 가능함
# 해석 : soup 객체에서 find 함수를 이용하여 "class = Nbtn_upload"인 a 태그를 찾아서 출력해 줘

# print(soup.find(attrs={"class":"Nbtn_upload"}))             # ~ "class = Nbtn_upload"인 어떤 태그를 찾아서 출력해 줘




# 네이버 웹툰 메인 화면에서 인기급상승 만화 -> 1위 작품에 커서 올려서 개발자모드로 확인 -> 1위 작품의 class 값 확인 및 복붙

# print(soup.find("li", attrs={"class":"rank01"}))             # 해석 : li 태그 내 첫번째 rank01 클래스를 출력

rank1 = soup.find("li", attrs={"class":"rank01"})           
# print(rank1.a)                                              # 해석 : li 태그 내 rank01 클래스 내에서 첫번째 a 로 시작하는 값 부분만 출력

print(rank1.a.get_text())



# 형제자매 이동 (sibling)

# print(rank1.next_sibling)                                   # 변수.next_sibling : 다음 형제를 불러오는 명령어 (특정 이유로 안먹힐 경우 .next_sibling을 한번더 치면 됨 (개행처리))

# rank2 = rank1.next_sibling.next_sibling
rank2 = rank1.find_next_sibling("li")                       # 변수.find_next_sibling("특정 클래스") : 개행처리 고민 없이 다음 형제로 이동 가능
print(rank2.a.get_text())

# rank3 = rank2.next_sibling.next_sibling
rank3 = rank2.find_next_sibling("li")
print(rank3.a.get_text())

# rank2 = rank3.previous_sibling.previous_sibling             # 변수.previous_sibling : 이전 형제를 불러오는 명령어 (개헝처리 때문에 인식 안되면 .previou_sibling 2번 적기)
rank2 = rank3.find_previous_sibling("li")
print(rank2.a.get_text())


print("\n<줄 변경>\n")
# 형제자매 정보 한번에 이동 (siblings)
print(rank1.find_next_siblings("li"))                       # 변수.find_next_siblings("특정값") : 변수와 같은 계층의 다음에 오는 모든 값이 출력됨



print("\n<줄 변경>\n")
# 부모 이동
print(rank1.parent)                                         # 태그.parent : rank1보다 한단계 위의 태그값 출력



print("\n<줄 변경>\n")
# 
webtoon = soup.find("a", text="신의 탑-3부 79화")           # 객체.find("태그", text="웹툰제목") : 웹툰제목이 속해있는 a 태그 값을 모두 츌력
print(webtoon)