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

## isinstance 함수

특정 객체가 특정 클래스의 인스턴스인지 확인하는 함수.

사용법: isinstance(객체, 클래스)

```python
print(isinstance(3, int)) # True
print(isinstance('심교훈', str)) # True
print(isinstance('심교훈', int)) # False
```

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

print(isinstance(p1, Programmer)) # True
print(isinstance(p2, SoccerPlayer)) # True
print(isinstance(p2, Programmer)) # False
print(isinstance(p1, Person)) # True
```

### type 함수 vs isinstance 함수

어떤 객체의 type, class를 확인할 때는 크게 두 가지 방법이 있음.

- type(객체) is 클래스
- isinstance(객체, 클래스)

    ```python
    print(type(3) is int) # True
    print(isinstance(3, int)) # True
    ```

    isinstance() 함수는 부모 클래스에도 True를 반환.

    반면, type() is 방식은 부모 클래스에 대해서는 False를 반환.

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


    p1 = Programmer("심교훈", 35)

    print(isinstance(p1, Programmer)) # True
    print(isinstance(p1, Person)) # True 

    print(type(p1) is Programmer) # True
    print(type(p1) is Person) # False
    ```

## 클래스 속성

클래스를 정의할 때 메서드 밖에 존재하는 변수(속성)을 클래스 변수(속성)이라고 함.

```python
class Person:
    person_cnt = 0 # 클래스 변수

    def __init__(self, name, age):
        self.name = name # 인스턴스 변수
        self.age = age # 인스턴스 변수
        Person.person_cnt += 1
        print(f"현재까지 사람 객체 {Person.person_cnt}명 생성됨.")


person1 = Person("심교훈", 35) # 현재까지 사람 객체 1명 생성됨.
person2 = Person("문태호", 36) # 현재까지 사람 객체 2명 생성됨.

print(person1.person_cnt) # 2
print(person1.person_cnt) # 2
print(Person.person_cnt) # 2
```

클래스 안에서 클래스 속성에 접근할 떄는 "클래스명.변수명"으로 접근 가능.

클래스 밖에서 클래스 속성에 접근할 때는 "클래스명.변수명" 또는 "인스턴스명.변수명"으로 접근 가능.

인스턴스마다 독립적인 값을 갖지 않고, 같은 값을 공유.

## 클래스 메서드

class 내 메소드에 @classmethod 데코레이터가 붙은 것들을 클래스 메서드라고 함.

클래스 메서드의 첫 매개변수는 항상 cls.

```python
from datetime import datetime


class Person:
    person_cnt = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.add_person_cnt()

    @classmethod
    def add_person_cnt(cls):
        cls.person_cnt += 1

    @classmethod
    def print_person_cnt(cls):
        print(f"현재까지 {Person.person_cnt}명 생성됨.")
    
    @classmethod
    def from_year(cls, name, year): # 팩토리 메서드용 classmethod
        return cls(name, datetime.now().year - year + 1)


p1 = Person("심교훈", 35)
p2 = Person.from_year("문태호", 1987)

p1.print_person_cnt()
```

## 정적 메서드

class 내 메소드에 @staticmethod 데코레이터가 붙은 것들을 정적 메서드라고 함.

비슷한 기능을 수행하는 유틸리티 함수들을 하나의 클래스 안에 묶어두기 위한 용도로 많이 사용.

```python
class Calc:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def sub(x, y):
        return x - y

    @staticmethod
    def mul(x, y):
        return x * y

    @staticmethod
    def div(x, y):
        return x / y


print(Calc.add(5, 7)) # 12
print(Calc.sub(8, 3)) # 5
print(Calc.mul(4, 6)) # 24
print(Calc.div(9, 2)) # 4.5
```

---

## 클래스 실습

포켓몬 클래스를 하나 만든다.

포켓몬 클래스는 객체를 생성할 때 이름을 전달받는다.

포켓몬 클래스는 자기 이름을 소개하는 메서드를 갖는다.

포켓몬 클래스를 상속 받아서 피카추 클래스, 꼬부기 클래스를 만들 것.

피카추 클래스에는 피카추만의 능력을 메서드로 만들고, 꼬부기 클래스에는 꼬부기만의 능력을 메서드로 추가할 것.

만든 피카추 클래스와 꼬부기 클래스로 각각 1개의 인스턴스를 생성하여 가진 능력을 뽐낼 것.
