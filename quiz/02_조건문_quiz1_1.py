num = int(input("1에서 12사이의 정수를 입력해주세요: "))

if num in [3, 4, 5]:
    print("봄")
elif num in [6, 7, 8]:
    print("여름")
elif num in [9, 10, 11]:
    print("가을")
elif num in [12, 1, 2]:
    print("겨울")
else:
    print("1~12 사이의 숫자를 입력하세요")
