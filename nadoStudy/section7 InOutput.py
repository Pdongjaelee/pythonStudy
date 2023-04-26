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
# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 특정 자리수 까지만 표시 (소수점 3째 자리에서 반올리)
print("{0:.2f}".format(5/3))



## 파일 입출력
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")  # r은 read
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="") # end="" 는 별도의 줄바꿈 없이 출력
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8") #  encoding="utf8" 는 한글을 사용할거니까
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() # list 형태로 저장
# for line in lines:
#     print(line, end="")
#
# score_file.close()



## pickle
# pickle은 프로그램상에서 사용하고 있는 데이터를 파일 형태로 저장한다.
# 데이터를 파일 형태로 저장하고 가져와서 변수로 사용할 수 있는 유용한 라이브러리
import pickle
# profile_file = open("profile.pickle", "wb") #wb는 쓰기
# profile = {"이름":"이동구", "나이":30, "취미":["산책", "낮잠"]}
# print(profile)
# pickle.dump(profile, profile_file) #profile 에 있는 정보를  file 에 저장
# profile_file.close()

profile_file = open("profile.pickle", "rb") #r는 읽기 b는 binary
profile = pickle.load(profile_file) # file 에 있는 정보를 profile 에 불러오기
print(profile)
profile_file.close()


## with
import pickle
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "w", encoding="utf8") as study_file:
    print(study_file.read())

# 파일이 있다는 가정하에 with을 쓰면 매번 close 할 필요없이 with 한줄~ 두줄을 써서 가져온다.



## Quiz

# 매주 1회 작성해야 하는 보고서가 있다.
# 보고서 출력 형태
# - x 주차 주간보고 -
# 부서 :
# 이름 :
# 업무 요약 :

# 1추자 ~ 50주차까지의 보고서 파일을 만드는 프로그램 작성

# 조건 : 파일명은 '1주차.txt', '2주차.txt', ...

for i in range(1, 51):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 -".format(i))
        report_file.write("\n부서 :" ) #\n 줄바꿈 처리
        report_file.write("\n이름 :")
        report_file.write("\n업무 요약 :")
