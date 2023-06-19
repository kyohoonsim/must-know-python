class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"제 이름은 {self.name}이고, 나이는 {self.age}입니다.")


class Programmer(Person):
    def coding(self):
        print("저는 코딩을 합니다.") 


class SoccerPlayer(Person):
    def play_soccer(self):
        print("저는 축구를 합니다.")


p1 = Programmer("심교훈", 35)
p2 = SoccerPlayer("손흥민", 31)

p1.introduce()
p1.coding()

p2.introduce()
p2.play_soccer()