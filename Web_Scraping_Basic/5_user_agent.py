# User-Agent
# - 어떤 페이지를 보여줄까?       (접속한 기기(PC, 스마트폰) / 해당 국가 지역 등 User-Agent 정보를 통해 맞춤형 페이지를 보여줌)
# - 그런데 접속한게 사람이 맞아?  (페이지를 접속한게 봇이라고 생각하면 접속 권한을 주지 않을 수도 있음 -> User-Agent 정보를 입력해서 사람이 맞다고 인식시킬 수 있음)

# 3_request.py에서 작성한 코드 복붙 및 주석 삭제 (print 코드 삭제)



# user agent 확인 방법 -> 구글에서 user agent string 이라고 검색 (접속하는 브라우저에 따라 u.a. 값이 다름)

# https://www.whatismybrowser.com/detect/what-is-my-user-agent



import requests

url = "http://nadocoding.tistory.com"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
#           유저 에이전트 대/소문자, 하이펀 확실하게 적어야 함!!!

res = requests.get(url, headers=headers)                        # url 페이지에 접속할 때, headers에 정의된 user agent 값을 넘겨줌
res.raise_for_status()

with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)                                      






# html, xpath, request, 정규식, user_agent 5개 개념을 알면 웹 스크래핑을 할 수 있음!