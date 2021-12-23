# Headless Chrome을 쓸 때 주의점
# : 구글 무비에서는 user-agent를 설정하지 않아도 headless chrome 접속 시 정상 작동하나,
#   일부 사이트에서는 봇 등으로 오해받아 접속 차단 될 수 있음
#   -> 그럴 때는 options.add_argument("user-agent=~~~") 코드를 추가하면 사람이 접속하는 것으로 인식하여 정상 작동 됨!



# 17_headless_chrome 파일 코드 복붙 후 코드 추가



import time
from selenium import webdriver

from bs4 import BeautifulSoup



options = webdriver.ChromeOptions()                                     

options.add_experimental_option("excludeSwitches", ["enable-logging"])

options.headless = True
options.add_argument("window-size=1920x1080")                               # 해당 코드를 넣지 않으면 headless chrome 접속으로 인식되어 일부 사이트에서 접속 차단될 수 있음



# headless chrome으로 접속 시 사이트에서 봇 접속 등으로 차단 당하는걸 방지하는 기능 (w.m.u.a.? 사이트에서 user-agent값 복붙해서 입력)
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36")



browser = webdriver.Chrome(options=options) 

browser.maximize_window()


# what is my user agent? 사이트에서 user-agent 값 불러오기
url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)



# 사이트에서 표시된 내 크롬 user-agent 값 : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36

# 코드를 통해 출력한 user-agent 값       : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/92.0.4515.107 Safari/537.36
# -> headless chrome을 사용해서 사이트 접속 시 user-agent 값 뒤에 'HeadlessChrome/92.0.4515.107 Safari/537.36' 꼬리표가 뜰 수 있음
# -> 일부 사이트에서 headless chrome 접속을 차단할 수 있으므로 별도의 조취가 필요함

# -> 위에 options.add_argument("user-agent=~~~") 코드를 추가한 후 코드를 재실행하면
#    Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36
#    으로 해당 사이트가 headless chrome 이 아닌 일반 chrome 창을 띄운걸로 인식! (해당 사이트에서 차단되는 것 방지 가능!!)
