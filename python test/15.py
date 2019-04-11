class Calculate:
    def __init__(self):
        self.a = None
        self.b = None
        self.add_count = 0
        self.sub_count = 0
        self.mul_count = 0
        self.div_count = 0

    def set_data(self, a, b):
        self.a = a
        self.b = b

    def is_set_data(self):
        if self.a != None and self.b != None:
            return True

        else:
            return False

    def add(self):
        if(self.is_set_data):
            self.add_count += 1
            return self.a + self.b

        else:
            return "데이터 설정을 하세요"

    def sub(self):
        if(self.is_set_data):
            self.sub_count += 1
            return self.a - self.b

        else:
            return "데이터 설정을 하세요"

    def mul(self):
        if(self.is_set_data):
            self.mul_count += 1
            return self.a * self.b

        else:
            return "데이터 설정을 하세요"

    def div(self):
        if(self.is_set_data):
            self.div_count += 1
            return self.a / self.b

        else:
            return "데이터 설정을 하세요"

    def showCount(self):
        print("덧셈 : ", self.add_count)
        print("뺄셈 : ", self.sub_count)
        print("곱셈 : ", self.mul_count)
        print("나눗셈 : ", self.div_count)


cal = Calculate()
num1 = int(input("num1를 입력하세요 : "))
num2 = int(input("num2를 입력하세요 : "))

cal.set_data(num1, num2)

print(num1, " + ", num2, " = ", cal.add())
print(num1, " - ", num2, " = ", cal.sub())
print(num1, " * ", num2, " = ", cal.mul())
print(num1, " / ", num2, " = ", cal.div())

print(cal.showCount())
