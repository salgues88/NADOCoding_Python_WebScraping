import requests
from bs4 import BeautifulSoup



for year in range(2015,2021):                                       # 반복문을 통해 2015 ~ 2020년 영화 불러오기, 해당년도 값은 year로 반환

    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)

    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class":"thumb_img"})

    for idx, image in enumerate(images):
        # print(image["src"])
        image_url = image["src"]
        if image_url.startswith("//"):                               # 변수.startswith("문자열") : 괄호 안에 적은 문자열로 시작하는지를 확인하는 함수
            image_url = "http:" + image_url


        print(image_url)
        image_res = requests.get(image_url)
        image_res.raise_for_status()

        with open("movie{}_{}.jpg".format(year, idx + 1), "wb") as f:        # 이미지는 바이너리 -> wb
            f.write(image_res.content)                              # .content : 이미지 데이터를 가져올 때 사용 (텍스트는 . text)
        
        if idx >= 4:                                                # 상위 5개 이미지 까지만 받겠다는 뜻
            break

