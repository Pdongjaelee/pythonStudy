
# 변수 설정
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


# 변수 quiz

station = "사당"
print(station + "행 열차가 들어오고 있습니다.")
station = "신도림"
print(station + "행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station + "행 열차가 들어오고 있습니다.")


# 연산자

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


# 절대값

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


# 랜덤함수
from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성

print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성

print(randint(1, 46)) # 1 ~ 45 이하의 임의의 값 생성



# 연산자 quiz

from random import *
day = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월" + str(day) + "일로 선정되었습니다.")



# 문자열
sentence = '나는 소년이다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3) #sentence 뒤 숫자는 print 순서






