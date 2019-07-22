student = {'혜린' : 100 , '잔나비' : 95, '김철수' : 50 , '이영자' : 70}

print("1. 학생개인성적조회","2. 학급전체평균성적 조회", "3. 종료",sep='\n')

while(True):
    num=int(input("메뉴를 선택하세요 : "))

    if num==1:
        name = input('성적조회를 원하는 학생의 이름을 입력하세요 : ')
        print(name)

    elif num==2:
        pass

    else:
        breakstudent = {'혜린' : 100 , '잔나비' : 95, '김철수' : 50 , '이영자' : 70}

print("1. 학생개인성적조회","2. 학급전체평균성적 조회", "3. 종료",sep='\n')

while(True):
    num=int(input("메뉴를 선택하세요 : "))

    if num==1:
        name = input('성적조회를 원하는 학생의 이름을 입력하세요 : ')
        print(name,"학생의 성적은",student[name],'점 입니다')

    elif num==2:
        aver = 0
        for grade in student.values():
            aver = aver + grade

        print("학급전체평균성적은 ",aver/len(student), "점 입니다.")

    else:
        break
