# 클래스

객체 지향 프로그래밍 언어의 핵심.

클래스는 틀, 객체는 틀로 찍어낸 결과물.

클래스는 붕어빵 틀, 객체는 붕어빵.

속성과 메소드로 구성.

## 클래스가 필요한 이유

```python
name1 = "심교훈"
age1 = 35
print(f"제 이름은 {name1}이고, 나이는 {age1}입니다.")
print(f"제 성은 {name1[0]}씨입니다.")

name2 = "문태호"
age2 = 36
print(f"제 이름은 {name2}이고, 나이는 {age2}입니다.")
print(f"제 성은 {name2[0]}씨입니다.")

name3 = "황병일"
age3 = 37
print(f"제 이름은 {name3}이고, 나이는 {age3}입니다.")
print(f"제 성은 {name3[0]}씨입니다.")
```

위 코드는 중복된 부분이 많음. 그러나 함수로 처리하기에는 조금 애매함. 어떤 존재의 속성과 능력으로 구성된 것은 클래스로 표현하기 좋음.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"제 이름은 {self.name}이고, 나이는 {self.age}입니다.")

    def introduce_family_name(self):
        print(f"제 성은 {self.name[0]}씨입니다.")


p1 = Person("심교훈", 35)
p1.introduce()
p1.introduce_family_name()

p2 = Person("문태호", 36)
p2.introduce()
p2.introduce_family_name()

p3 = Person("황병일", 37)
p3.introduce()
p3.introduce_family_name()
```

## 상속

```python
class Programmer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"제 이름은 {self.name}이고, 나이는 {self.age}입니다.")

    def coding(self):
        print("저는 코딩을 합니다.")     


class SoccerPlayer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"제 이름은 {self.name}이고, 나이는 {self.age}입니다.")

    def play_soccer(self):
        print("저는 축구를 합니다.")


p1 = Programmer("심교훈", 35)
p2 = SoccerPlayer("손흥민", 31)

p1.introduce()
p1.coding()

p2.introduce()
p2.play_soccer()
```

위에서 Programmer 클래스와 SoccerPlayer 클래스에는 공통된 부분이 있다. 프로그래머와 축구 선수 모두 사람이기 때문에 공통된 부분이 존재한다고 볼 수 있다. 그러므로 공통된 부분으로 사람 클래스를 만든 후에 사람 클래스를 상속 받아 프로그래머, 축구선수 클래스를 만들 수 있다.

```python
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
```

## 정적메서드


## 클래스메서드
