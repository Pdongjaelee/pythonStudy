### section 1 ~ 3


## 변수 설정
animal = "강아지"
name = "리동구"
age = 4
hobby = "산책"
is_adult = age >= 3


print("우리집 " + animal + "의 이름은 " + name + "예요")
print(name + "는 " +str(age) + "살이며, " + hobby + "을 아주 좋아해요")
hobby = "공놀이" #변수 설정은 그 밑에 줄부터 적용된다.
print(name + "는 " +str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))


## 변수 quiz

station = "사당"
print(station + "행 열차가 들어오고 있습니다.")
station = "신도림"
print(station + "행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station + "행 열차가 들어오고 있습니다.")


## 연산자

print(2**3) # 2^3 = 8
print(5%3) # 나머지 구하기 = 2
print(5//3) # 나누기 몫 구하기 = 1

print(3 == 3) # 비교 True / False
print(3 + 4 == 7) # 비교 True / False

print(1 != 3) #  !는 not True #True
print(not (1 != 3)) #  !는 not True #False

print((3 > 0) and (3 < 5)) #True
print((3 > 0) & (3 < 5)) #True

print((3 > 0) or (3 < 5)) #True
print((3 > 0) | (3 < 5)) #True


## 절대값

print(abs(-5)) # 5
print(pow(4, 2)) # 4^2 = 4*4 = 16
print(max(5, 12)) # 둘 중 큰 값 12
print(min(5, 12)) # 둘 중 작은 값 12
print(round(3.14)) # 반올림 3
print(round(4.99)) # 반올림 5

from math import *
print(floor(4.99)) # 내림. 4
print(ceil(3.14)) # 올림. 4
print(sqrt(16)) # 제곱근. 4


## 랜덤함수
from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성

print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성

print(randint(1, 46)) # 1 ~ 45 이하의 임의의 값 생성



## 연산자 quiz

from random import *
day = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월" + str(day) + "일로 선정되었습니다.")



## 문자열
sentence = '나는 소년이다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3) #sentence 뒤 숫자는 print 순서


## 슬라이싱
jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0 부터 2 직전까지 (0, 1)
print("월 : " + jumin[2:4]) # 0 부터 2 직전까지
print("일 : " + jumin[4:6]) # 0 부터 2 직전까지

print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지
print("뒤 7자리 : " + jumin[7:]) # 7부터 끝까지
print("뒤 7자리(뒤에부터) : " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지

## 문자열 처리함수

python = "Python in Amazing"
print(python.lower()) # 소문자
print(python.upper()) # 대문자
print(python[0].isupper()) # 0번째가 대문자인지 true/false
print(len(python)) # 해당 변수 길이
print(python.replace("Python", "Java")) # 변수 내용을 바꿔준다.

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("Java")) # 해당 변수에는 Java가 없으므로 -1 출력, error 안내고 계속 프로그램 진행시키려고 할 때
# print(python.index("Java")) # 해당 변수에는 Java가 없으므로 그냥 바로 error를 내버린다. - find와 차이

print(python.count("n")) # 해당 변수에 n이 몇개인지 출력

## 문자열 포맷

# 방법 1
print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple은 %c로 시작해요." % "A")

print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간")) # 두개 이상을 넣고 싶을 때는 뒤에 괄호 만들고 안에 넣기

# 방법 2
print("나는 {}살입니다." .format(20))
print("나는 {}색괴 {}색을 좋아해요." .format("파란", "빨간"))
print("나는 {0}색괴 {1}색을 좋아해요." .format("파란", "빨간"))
print("나는 {1}색괴 {0}색을 좋아해요." .format("파란", "빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요." .format( color="빨간", age = 20))

# 방법 4
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")



## 탈출문자
# \n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")

# \" \' : 문장 내에서 따옴표
print("저는 '나도코딩'입니다.")
print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\"입니다.")
print("저는 \'나도코딩\'입니다.")

# \\ : 문장 내에서는  \로 읽힘
# print("C:\\Python37\\python.exe C:\\Users\\USER\\PycharmProjects\\pythonStudy\\nadoStudy.py")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")

# \b : 백스페이스 (한 글자 삭제)
print("Redd \bApple")

# \t : 탭
print("Red\tApple")


## 문자열 Quiz

#Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
#ex) http://naver.com
# 규칙 1 : http:// 부분은 제외 => naver.com
# 규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성

# ex) 생성된 비밀번호 : nav51!

url = "http://naver.com"
my_str = url.replace("http://", "") # 규칙1
print(my_str)
my_str = my_str[:my_str.index(".")] # 규칙2
#m_str[0:5] -> 0 ~ 5 직전까지. (0, 1, 2, 3, 4)
print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1} 입니다.".format(url, password))





