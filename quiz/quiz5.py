class Pokemon:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"제 이름은 {self.name}입니다.")


class Pikachu(Pokemon):
    def attack_electric(self):
        print("전기 공격")


class Ggobugi(Pokemon):
    def attack_water(self):
        print("물 공격")


pikachu1 = Pikachu("피카츄1")
ggobugi1 = Ggobugi("꼬부기1")

pikachu1.introduce()
ggobugi1.introduce()
pikachu1.attack_electric()
ggobugi1.attack_water()