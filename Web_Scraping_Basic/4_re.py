# 정규식 : 정규 표현식(Regular Expressions)은 복잡한 문자열을 처리할 때 사용하는 기법으로,
#          파이썬만의 고유 문법이 아니라 문자열을 처리하는 모든 곳에서 사용한다. 
#          정규 표현식을 배우는 것은 파이썬을 배우는 것과는 또 다른 영역의 과제이다.


# 정규식은 워낙 많아서 모두 다를 순 없음 -> 웹 스크래핑에 필요한 부분만 다룸

# ex. 주민등록번호      900101-111111 (O), abcdef-111111 (X)
# ex2. IP 주소          192.168.0.1 (O), 1000.2000.3000.4 (X)


########################################################################


# 정규식 사용방법 정리

# 0) import re                     : 정규식 함수 불러오기

# 1) p = re.compile("원하는 형태")  : 정규식을 사용하고자 하는 원하는 형태 입력
### 정규식 원하는 형태 예시
##### . (ca.e) : 하나의 문자를 의미        ex. cafe, case, care (O) | caffe, calle (X)
##### ^ (^de)  : 문자열의 시작             ex. destiny, destination, desert (O) | fade, shade (X)
##### $ (se$)  : 문자열의 끝               ex. case, base (O) | face, seven (X)
##### 그 외 기타 형태 (나도코딩 수업에서는 이정도면 충분함)

# 2-1) m = p.match("비교할 문자열")   : 주어진 문자열이 처음부터 일치하는지 확인 (매칭되면 매칭값 출력, 안되면 출력 X)

# 2-2) m = p.search("비교할 문자열")  : 주어진 문자열 중 일치하는게 있는지 확인 (.group(), .string, .start(), .end(), .span() 등과 함께 사용)

# 2-3) lst = p.findall("비교할문자열"): 일치하는 모든 것을 '리스트'형태로 반환



# 정규식 공부 추천 사이트
# https://www.w3schools.com/python/python_regex.asp
# https://docs.python.org/3/library/re.html


########################################################################


import re                                               # import re : 정규식 라이브러리

# 교통사고가 났는데 목격자는 차량번호를 ca?e로 기억함 -> 유사 단어 : care, cafe, case, cave, ...

# -> 하나하나 대입해보면 caae, cabe, cace, ... 로 무수히 많아서 찾기 어려움 -> 정규식을 사용하여 찾기 가능

p = re.compile("ca.e")
# re.compile()에서는 아래의 방법으로 정규식 사용 가능
### . (ca.e) : 하나의 문자를 의미 ex. cafe, case, care (O) | caffe, calle (X)
### ^ (^de)  : 문자열의 시작      ex. destiny, destination, desert (O) | fade, shade (X)
### $ (se$)  : 문자열의 끝       ex. case, base (O) | face, seven (X)
### 그 외 기타 형태 (나도코딩 수업에서는 이정도면 충분함)




# 1. 변수.match() 예제

# def print_match(m):
#     if m:
#         print(m.group())                                # 정규식과 매칭되면 출력, 매칭되지 않으면 에러 출력
#     else:
#         print("매칭되지 않음")

# m = p.match("cadse")                                    # 변수.match() : (re 라이브러리에서) 주어진 문자열이 처음부터 일치하는지 확인
# print_match(m)                                          # -> good case (X), careless (O)




# 2. 변수.search() 예제

### 정규식 처리 자주쓰는 함수 정리


def print_match(m):
    if m:
        print("m.group():", m.group())                  ### 변수.group() : (re 라이브러리에서) 일치하는 문자열 반환 
        print("m.string:", m.string)                    ### 변수.string  : (re 라이브러리에서) 입력받은 문자열 (string은 함수X 변수O -> 괄호 없이 사용함)
        print("m.start():", m.start())                  ### 변수.start() : (re 라이브러리에서) 일치하는 문자열의 시작 인덱스
        print("M.end():", m.end())                      ### 변수.end()   : (re 라이브러리에서) 일치하는 문자열의 끝 인덱스
        print("M.span():", m.span())                    ### 변수.span()  : (re 라이브러리에서) 일치하는 문자열의 시작 / 끝 인덱스
    else:
        print("매칭되지 않음")

m = p.search("careless")                                # 변수.search() : (re 라이브러리에서) 주어진 문자열 중 일치하는게 있는지 확인
print_match(m)                                          # ex. good care, careless, case (O)

# ca.e 정규식에 careless 입력 시
# -> m.group(): care (일치하는 문자열 반환), m.string: careless (입력받은 문자열), 
#    m.start(): 0 (일치하는 문자열 시작 인덱스), M.end(): 4 (일치하는 문자열 끝 인덱스), M.span(): (0, 4) (~ 시작 / 끝 인덱스)



print("\n")
# 3. 변수.findall() 예제

lst = p.findall("careless cafe")                          # 변수.findall() : 일치하는 모든 것을 '리스트' 형태로 반환
print(lst)                                                # 출력값 : ['care', 'cafe']





