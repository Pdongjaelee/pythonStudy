# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 딕셔너리
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 예제 1

names = ['kim', 'park', 'cho', 'lee']

for n in names:
    print(n)

# 예제 2
# 딕셔너리
my_info = {
    "name": 'lee',
    "age": 33
}

# 이 때 반복할 때 value는 가져오지 않고 key만 가져온다.

for k in my_info:
    print('key:', my_info.get(k)) # my_info.get(k) = my_info[key]

for v in my_info.values():
    print('value :', v)



# 구구단 예시 출력
for i in range(2, 10):
    for j in range(1, 10):
        # {:4d} : 4자리의 정수형으로 .format(i *j),: ixj, end='' : 줄바꿈이 되지않게
        print('{:4d}'.format(i *j), end='')
    print()




# 변환 예제
# name2 = 'aceman'
#
# print('Reversed', reversed(name2))
# print('List', list(reversed(name2)))
# print('Tuple', tuple(reversed(name2)))




