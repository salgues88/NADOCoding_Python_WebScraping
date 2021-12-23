# Selenium : 웹페이지 테스트 자동화용 프레임워크

# pip install selenium

# 셀레늄을 사용하기 위해 웹 드라이버를 추가 설치해야함 (웹 드라이버는 익플/크롬/파폭 등에서 각각의 라이브러리 존재 -> 본 강의에선 크롬 드라이버 설치)
# 내 컴퓨터에 설치된 크롬 버전과 호환이 되는 웹 드라이버를 설치해야 함
# chrome 실햄 -> 주소창에서 chrome://version 확인 (92.0.4515.107)-> 구글에서 chrome driver 검색 -> 버전과 호환되는 드라이버 다운 (If you are using Chrome version 92, please download ChromeDriver 92.0.4515.43)
# 다운받은 크롬 드라이버를 PhythonWorkSpace 폴더에 넣고 압축해제해서 나온 exe 파일을 이용해서 셀레늄 코딩


# Tip. 터미널 관련 팁 
### 강제종료 : ctrl + C, python 직접 입력 모드 시작 : python, python 직접 입력 모드 종료 : exit()



# 셀레늄 기초 강의는 터미널에서 바로 작업 수행 (나도코딩 파이썬 활용3 3:02:41 강의 참고)
# (∵ vscode에 코드 작성 후 실행 시 매번 새로운 창이 뜨므로 실시간 반응을 보기 어려움 -> terminal에 파이썬 직접 입력 시 바로바로 업데이트가 가능해서 판단 가능)


# 셀레늄 심화 예제 (네이버 로그인)

import time
from selenium import webdriver

options = webdriver.ChromeOptions()                                     # webdriver.Chrome으로 불러오니 계속 에러표시가 떠서 에러표시 안나게 하는 방법 적용 (by 구글링)
options.add_experimental_option("excludeSwitches", ["enable-logging"])

browser = webdriver.Chrome(options=options)                             
# webdriver exe 파일이 동일 경로이면 .Chrome()안에 아무것도 안적어도 되고, 만약에 다르면 exe 파일 경로를 .Chrome("경로")안에 적어줘야 함
# (원래는 webdriver.Chrome()으로 끝나나, 에러표시가 계속 떠서 options로 에러 표시 없앰)



# 1. 네이버 이동
browser.get("https://www.naver.com")


# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()


# 3. ID / PW 입력 (일부러 틀린 아이디, 패스워드 입력)
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("naver_pw")

time.sleep(3)


# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()                         # 2. 로그인 버튼 클릭처럼 2줄로 만들수도 있고, 한줄에 코드 작성 다 해도 됨

time.sleep(3)


# 5. id를 새로 입력
browser.find_element_by_id("id").clear()                                # 기존 id가 삽입된 내용을 클리어
browser.find_element_by_id("id").send_keys("my_id")                     # 실행하니 너무 빨리 정보가 전달되어 봇 취급받음 -> 딜레이 필요


# 6. html 정보 출력
print(browser.page_source)


# 7. 브라우저 종료
# browser.close()                                                         # 현재 탭만 종료
browser.quit()                                                          # 전체 탭 종료





# Selenium에 대해 더 알고 싶으면 구글에서 selenium with python으로 검색
# -> Selenium with Python 사이트에 접속해서 필요한 기능을 공부하면 됨 (https://selenium-python.readthedocs.io/)