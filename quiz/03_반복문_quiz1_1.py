def show_happy_point(point):
    print(f"현재 강아지 행복 점수: {point}")


print("="*30)
print("강아지 돌보는 로봇 v1.0")
print("="*30)

happy_point = 0

while True:
    sel = input("\n1.먹이주기 2.놀아주기 3.산책하기 4.목욕하기 q.프로그램종료 >> ")

    if sel == "1":
        print("먹이를 줍니다.")
        happy_point += 5
        show_happy_point(happy_point)
    elif sel == "2":
        print("놀아 줍니다.")
        happy_point += 7
        show_happy_point(happy_point)
    elif sel == "3":
        print("산책을 시킵니다.")
        happy_point += 10
        show_happy_point(happy_point)
    elif sel == "4":
        print("목욕을 시킵니다.")
        happy_point += 3
        show_happy_point(happy_point)
    elif sel == "q":
        print("프로그램을 종료합니다.")
        show_happy_point(happy_point)
        break
