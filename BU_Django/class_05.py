# class 클래스():
#     변수 = 1
        # 또는
        # def __init__(self):
        #     self.qustn = 1

#     def 변수변경(self):
#         self.변수 = 3  #  초깃값 변경


class 업무():

    아침업무유무 = False

    def 아침업무체크(self):
        self.아침업무유무 = True

    def 아침업무(self, 상자):
        for 물건 in 상자:
            if 물건 == '사과':
                print(f"'{물건}' 냉장실에 넣기")
            elif 물건 == '아이스크림':
                print(f"'{물건}' 냉동실에 넣기")
            else:
                print(f"'{물건}'은 폐기 처분")

        self.아침업무체크()


출근 = True

if 출근:
    상자 = ["콩", "콩", "콩", "사과"]

    사원1_업무 = 업무()
    print(사원1_업무.아침업무유무) # false
    print(사원1_업무.아침업무(상자))
    print(사원1_업무.아침업무유무) # true

    # 사원2_업무 = 업무()
    # print(사원2_업무.아침업무유무)
