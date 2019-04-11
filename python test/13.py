num = int(input("1부터 9 사이 숫자를 입력하세요 : "))

for i in range(1, num+1):
    if i % 2 != 0:
        for j in range(1, num+1):
            if j % 2 != 0:
                print(j, end='  ')
    else:
        for j in range(1, num+1):
            if j % 2 == 0:
                print(' ', j, end='')
    print('\n')
