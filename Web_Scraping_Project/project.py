import requests
from bs4 import BeautifulSoup
import re



# 뷰티풀 수프 함수 (url 접속할 때 마다 res 등을 매번 적어야 하므로 함수로 만들고 반환) (주어진 url 정보를 가지고 뷰티풀 수프 객체를 만드는 과정)
def create_soup(url):

    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup                                                                                     # 뷰티풀 수프 객체 값을 외부로 반환



# 헤드라인 뉴스 및 IT 뉴스에서 반복해석 출력되는 print 부분을 따로 함수로 만듬
def print_news(idx, title, link):
    print("{}. {}".format(idx+1, title))                                            # 해석 : 인덱스는 0부터 시작하므로 idx뒤에 +1을 적용함
    print("   (링크 : {})".format(link))



# 오늘의 날씨 웹 스크래핑 함수
def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%B6%80%EC%82%B0+%EB%82%A0%EC%94%A8"
    soup = create_soup(url)                                                                         


    # 오늘 날씨 평가 (ex. 흐림, 어제보다 xx℃ 높아요)
    cast = soup.find("p", attrs={"class":"cast_txt"}).get_text()

    # 현재 xx℃ (최저 aa℃ / 최고 bb℃)
    curr_temp = soup.find("p", attrs={"class":"info_temperature"}).get_text().replace("도씨", "")   # .replace("기존 문자열", "바꿀 문자열")
    min_temp = soup.find("span", attrs={"class":"min"}).get_text()
    max_temp = soup.find("span", attrs={"class":"max"}).get_text()

    # 오전 강수확률 cc℃ / 오후 강수확률 dd℃
    morning_rain_rate = soup.find("span", attrs={"class":"point_time morning"}).get_text().strip()  # .strip() : html 내부 문자의 공백 제거 기능
    afternoon_rain_rate = soup.find("span", attrs={"class":"point_time afternoon"}).get_text().strip()

    # 미세먼지   ee㎍/㎥ 좋음
    # 초미세먼지 ff㎍/㎥ 좋음
    dust = soup.find("dl", attrs={"class":"indicator"})
    pm10 = dust.find_all("dd")[0].get_text()                                            # 해석 : dl class 내 모든 dd class 중 첫번째 것[0](1v1)의 텍스트를 가져오기
    pm25 = dust.find_all("dd")[1].get_text()                                            # 해석 : dl class 내 모든 dd class 중 두번째 것[1](1v2)의 텍스트를 가져오기

    # 출력
    print(cast)

    print(f"현재 {curr_temp} (최고 {max_temp}, 최저 {min_temp})")

    print("오전 {} / 오후 {}".format(morning_rain_rate, afternoon_rain_rate))

    print(f"미세먼지 {pm10}")
    print(f"초미세먼지 {pm25}")
    print()                                                                 # 줄바꿈 용



# 헤드라인 뉴스 웹 스크래핑 함수                                                            ()
def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li", limit=3)   # 해석 : ul class 밑의 li 값을 3개 까지만 찾고 들고오기 (limit=3)

    for idx, news in enumerate(news_list):                                              # 해석 : 출력 결과를 반복해서 가져올 때 1, 2, 3 등 인덱스로 표시하기 위해 enumerate 사용
        title = news.find("a").get_text().strip()                                      
        link = news.find("a")["href"]                                                   # 해석 : a href 뒤의 주소 정보 가져옴, url 주소가 생략되어서 +로 연결

        print_news(idx, title, link)
    print()




# IT 뉴스 웹 스크래핑 함수
def scrape_it_news():
    print("[IT 뉴스]")
    url = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"type06_headline"}).find_all("li", limit=3)
    for idx, news in enumerate(news_list):

        a_idx = 0                                                                           
        img = news.find("img")                                                          # 해석 : img 글자가 있는 태그 찾기
        if img:
            a_idx = 1                                                                   # 해석 : img 태그가 잇으면 1번째 a 태그 정보를 사용하겠다 (이미지 태그가 없으면 0번째를 사용하겠다)

        title = news.find_all("a")[a_idx].get_text().strip()                            # 해석 : a 태그 정보들 중 이미지가 없으면 0번째 정보 불러오고, img가 있으면 1번째 정보 불러오기
        link = url + news.find_all("a")[a_idx]["href"]                                  # 해석 : a href 뒤의 주소 정보 가져옴, url 주소가 생략되어서 +로 연결
        print_news(idx, title, link)
    print()




# [오늘의 영어 회화]
# (영어 지문)
# Jason : ...
# Kim : ...

# (한글 지문)
# Jason : ...
# Kim : ... 


# 오늘의 영어 회화 (해커스 토익) 함수
def scrape_english():
    print("[오늘의 영어 회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = create_soup(url)
    sentences = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})    # 해석 : 해커스 지문의 id가 conv_kor_t2, t3, ... 형태 -> 정규식으로 표현!

    # 한글, 영어문장 포함 현재 8문장이 있다고 가정 -> 영어문장을 호출하기 위해 5~8번 문장(index 기준 4~7)을 슬라이싱으로 잘라서 호출!
    print("(영어 지문)")
    for sentence in sentences[len(sentences)//2:]:                              # 해석 : 1) 나누다보면 소숫점 발생 가능성 존재 -> //로 몫만 남김, 2) 나누기 2의 정수값부터 마지막까지 (4:마지막)
        print(sentence.get_text().strip())
    print()
    
    # 한글, 영어문장 포함 현재 8문장이 있다고 가정 -> 한글문장을 호출하기 위해 1~4번 문장(index 기준 0~3)을 슬라이싱으로 잘라서 호출!
    print("(한글 지문")
    for sentence in sentences[:len(sentences)//2]:                              # 해석 : 1) 나누다보면 소숫점 발생 가능성 존재 -> //로 몫만 남김, 2) 0부터 나누기 2의 정수값까지 (0:4 직전)
        print(sentence.get_text().strip())
    print()





if __name__ == "__main__":                                                  # 해석 : __name__이라는 변수의 값이 __main__이라면 아래의 코드를 실행하라 (메인 함수 선언)
    scrape_weather()                                                        # 오늘의 날씨 정보 가져오기
    scrape_headline_news()                                                  # 헤드라인 뉴스 정보 가져오기
    scrape_it_news()                                                        # IT 뉴스 정보 가져오기
    scrape_english()                                                        # 오늘의 영어 회화 가져오기


