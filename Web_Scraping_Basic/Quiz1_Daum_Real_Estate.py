# Quiz1. 부동산 매물(송파 헬리오시티) 정보를 스크래핑 하는 프로그램을 만드시오




# ※ 다음 부동산에 '매물'항목이 아예 사라져서 기존 코드로 테스트 하는게 불가능함 -> 다음 강의로 패스!!!




# [조회 조건]
# 1) http://daum.net 접속
# 2) '송파 헬리오시티' 검색
# 3) 다음 부동산 부분에 나오는 결과 정보



# [출력 결과]
# ==============매물1==============
# 거래 : 매매
# 면적 : 84/59 (공급/전용)
# 가격 : 165,000 (만원)
# 동 : 214동
# 층 : 고/232

# ==============매물2==============
# ...



# [주의사항]
# - 실습하는 시점에 위 매물이 없다면 다른 것으로 대체 가능










# 해답2 (나) (웹페이지 개발자 모드 div 찾는데서 막힘, 나도코딩 힌트보고 재개)

import requests
from bs4 import BeautifulSoup

url = "https://realty.daum.net/home/apt/danjis/38487"

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

with open("quiz1_daum_real_estate.html", "w", encoding="utf8") as f:
    f.write(soup.prettify())



#items = soup.find_all("div", attrs={"class":""})
# print(len(items))

# for 반복문으로 나중에 넣기

# for item in items:
#     deal = item.find("div", attrs={"class":""})
#     print(deal)
