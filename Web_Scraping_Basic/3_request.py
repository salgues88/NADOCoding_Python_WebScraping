# pip install requests 설치

import requests
res = requests.get("http://www.google.com")
# res = requests.get("http://nadocoding.tistory.com")
print("응답코드 :", res.status_code)                         # 변수.status_code : 응답속도 확인 (200 : 정상, 403,404 : 웹 스크래핑 불가)


# 스테이터스 코드가 200 or 다른 숫자일 때 웹 스크래핑 가능 / 불가능 표시 방법
# if res.status_code == requests.codes.ok:                  # requests.codes.ok : 200 과 같은 뜻
#     print("정상입니다")
# else:
#     print("문제가 발생했습니다. [에러코드 :", res.status_code, "]")


# if문 대신 requests 내장함수를 이용하여 웹 스크래핑 가능 / 불가능 확인 방법
res.raise_for_status()
print("웹 스크래핑을 진행합니다")                             # 정상 : 프린트 문구 출력, 비정상 : 에러코드 및 오류 표시 (프린트 출력 X)

# res = requests.get("http://www.naver.com") \ res.raise_for_status()  <- 코딩 2문장으로 사이트 웹 스크래핑 가능 / 불가능 확인 가능

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf-8") as f:
    f.write(res.text)                                       # 스크래핑한 파일을 텍스트로 보기 힘드니 텍스트 파일에 내용 넣어서 텍스트 파일 생성
