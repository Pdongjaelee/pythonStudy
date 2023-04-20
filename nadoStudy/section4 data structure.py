### section4 자료 구조

## 리스트 []

# 지하철 칸별로 10명, 20명, 30명

subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호는 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하가 다음 정류장에서 다음 칸에 탐
subway.append("하하")  #append 맨 뒤에 추가할 때
print(subway)

# 정형돈을 유재석 / 조세호 사이에 태움
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop()) #pop 맨 뒤에 하나씩 뺌 #하하 out
# print(subway)
#
# print(subway.pop()) #박명수 out
# print(subway)
#
# print(subway.pop()) #조세호 out
# print(subway)
#
# print(subway.pop()) #정형돈 out
# print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort() #순서대로 정렬
print(num_list)

# 순서 뒤집기 가능
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
mix_list = ["조세호", 20, True]
# print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)



##사전
#사전에서는 키에 대한 중복이 허용되지 않는다.
#사전은 중괄호를 사용하면 된다.
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5]) #5가 없으므로 error가 발생해서 프로그램 종료
print(cabinet.get(5)) #get을 이용하면 값이 없음 none을 띄우고 계속 프로그램이 실행된다.
print(cabinet.get(5, "사용 가능"))

print(3 in cabinet) # True
print(5 in cabinet) # False


# 새 손님
print(cabinet)
cabinet[20] = "조세호"
cabinet[3] = "김종국"
print(cabinet)

# 간 손님
del cabinet[3]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 둘 다 출력
print(cabinet.items())

# 폐점 사전 정리
cabinet.clear()
print(cabinet)



## 튜플
# 튜플은 내용 변경이나 추가를 할 수 없으나 속도가 빠르다

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") # 이러면 error, 튜플은 add 기능 제공 안함

# 보통 이렇게 변수를 한줄 한줄 작성
# name = "동구"
# age = 4
# hobby = "산책"
# print(name, age, hobby)

# 튜플은 한 줄에 여러 변수 다 작성 가능
(name, age, hobby) = ("동구", 4, "산책")
print(name, age, hobby)




## 세트 (집합)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java와 python 을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java 할 수 있거나 python 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java 할 수 있지만 python 은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람을 추가
python.add("김태호")
print(python)

# java 를 잊어버린 사람
java.remove("김태호")
print(java)



## 자료구조의 변경
# 커피숍
menu = {"커피", "우유", "주스"} #set 형채
print(menu, type(menu))

menu = list(menu) #set ->list 형태로 바꿈
print(menu, type(menu))

menu = tuple(menu) #list ->tuple 형태로 바꿈
print(menu, type(menu))



## 자료구조 Quiz

# 댓글 이벤트

# (츨력 예제)
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst) #랜덤
# print(lst)
# print(sample(lst, 1)) #랜덤으로 lst 중에서 1개를 샘플링해서 뽑는다.

from random import *
users =range(1, 21) # 1부터 20까지 숫자를 생성
# print(type(users))
users = list(users)
# print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users, 4) #4명 중에서 1명은 치킨, 3명은 커피 / # 중복 제거

print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("--축하합니다--")
