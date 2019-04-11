list1 = ['구구단 프로그램을 실행합니다.', '1. 홀수 구구단', '2. 짝수 구구단', '3. 종료']

for i in range(len(list1)):
    print(list1[i])

while True:
    num = int(input("\n숫자를 입력하세요 : "))
    if num == 1:
        for i in range(3, 10):
            if i % 2 != 0:
                for j in range(1, 10):
                    print(i, " * ", j, " = ", i*j)

    elif num == 2:
        for i in range(3, 10):
            if i % 2 == 0:
                for j in range(1, 10):
                    print(i, " * ", j, " = ", i*j)

    elif num == 3:
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못 입력 하였습니다. 1~3번 숫자를 입력하세요.")
