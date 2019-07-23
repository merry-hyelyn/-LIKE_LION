class Class:
    def __init__(self,student):
        self.student = student

    def grade_personal(self,name):
        return self.student[name]

    def aver(self):
        aver = 0
        for grade in self.student.values():
            aver = aver + grade

        aver = aver/len(self.student)
        return round(aver,2)

def print_menu(student):
    print("1. 학생개인성적조회","2. 학급전체평균성적 조회", "3. 종료",sep='\n')

    while(True):
        num=int(input("메뉴를 선택하세요 : "))

        if num==1:
            name = input('성적조회를 원하는 학생의 이름을 입력하세요 : ')
            print(name,"학생의 성적은",student.grade_personal(name),'점 입니다')

        elif num==2:
            print("학급전체평균성적은 ",student.aver(), "점 입니다.")

        else:
            break

stu = {"hl":100, "jannabi" : 90, "bambi" : 60}
s1 = Class(stu)

print_menu(s1)
