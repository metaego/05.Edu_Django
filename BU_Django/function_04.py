def 더하기(첫번째, 두번째):
    return 첫번째 + 두번째

def 아침업무(상자):
    for 물건 in 상자:
        if 물건 == '사과':
            print(f"'{물건}' 냉장실에 넣기")
        elif 물건 == '아이스크림':
            print(f"'{물건}' 냉동실에 넣기")
        else:
            print(f"'{물건}'은 폐기 처분")

출근 = True

