
# separator 옵션, 원하는 포맷으로 출력할 때 sep 옵션 사용
print('P','Y','T', sep=',')
print('010','7777','7777', sep='-')


# end 옵션, 여러 출력 한 줄로 길게 붙일 때
print('Welcome to', end=' ')
print('IT News', end=' ')
print('Web Site')


# format 사용 (d : 3(정수), s : 'python'(문자열), f : 3.144444)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two')) #format 함수가 내부적으로 처리해줌

# %s (숫자는 전체 자릿수)
print('%10s' % ('nice'))
print('{:>10}'.format('nice')) #왼쪽에 10자리를 마련해주고 nice로 format해줘

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))


print('{:_>10}'.format('nice'))
print('{:^10}'.format('nice')) #중간 정열

print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy')) #5자리까지만 출력
print('{:10.5}'.format('pythonstudy')) #공간은 10이지만 출력은 5개만


# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print()


# %f