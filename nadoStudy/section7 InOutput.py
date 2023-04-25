###section7 입출력


## 표준입출력
# print("Python", "Java","js", sep=" , ", end="?") #sep를 통해 콤마를 할지 띄어쓰기를 할지 지정해줄 수 있다.
# print("무엇이 더 재밌을까요?") #end에 ?가 오면 다음에 오는 문장을 연달아서 출력한다.

# import sys
# print("Python", "Java",file=sys.stdout) #표준출력
# print("Python", "Java",file=sys.stderr) #표준에러로 출력

# 시험 성적
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     #print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")


# 은행 대기순번표
# 001, 002, 003, ...
# for num in range(1, 21):
#     print("대기번호 : "+ str(num).zfill(3))
#
# # answer = input("아무 값이나 입력하세요 :") # 사용자 입력을 통해서 값을 받게 되면 항상 문자열 형태로 받게된다.
# answer = 10
# print(type(answer))
# print("입력하신 값은" + answer + "입니다.")



## 다양한 출력포멧

# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))
# 양수일 떈 + 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
# 왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:_<10}".format(500))
# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(100000000000))


