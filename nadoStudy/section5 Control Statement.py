### section5 제어문

## if

# weather = input("오늘 날씨는 어때요? ")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else: # 어떤 조건도 아닐 때
#     print("준비물 필요 없어요.")

temp = int(input("기온은 어때요? "))
if 30 <= temp:
    print("너무 더워요.")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp and temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요")



## for
print("대기번호 : 1")
print("대기번호 : 2")
print("대기번호 : 3")
print("대기번호 : 4")

for waiting_no in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(1, 6): #1 ~ 6
    print("대기번호 : {0}".format(waiting_no))



## while

customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분")


customer = "토르"
person = "Unknown"

while person != customer :
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")




## continue, break

absent = [2, 5] # 결석
no_book = [7] # 책을 안가져옴
for student in range(1, 11): # 1,2,3,4,5,6,7,8,9,10
    if student in absent: # absent를 스킵하고 다음 번호 진행
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))



## 한줄 for

# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104.
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["iron mam", "tror", "i am groot"]
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["iron mam", "tror", "i am groot"]
students = [i.upper() for i in students]
print(students)



## 제어문 Quiz

from random import *
cnt = 0 # 총 탑승 승객 수
for i in range(1, 51): # 1 ~ 50 이라는 수 (승객)
    time = randrange(5, 51) # 5분 ~ 50분 소요 시간
    if 5 <= time <= 15: # 5분 ~ 15분 이내의 손님 (매칭 성공), 탑승 승객 수 증가 처리
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else: # 매칭 실패한 경우
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

print("총 탑승 승객 : {0} 분".format(cnt))