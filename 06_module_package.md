# 모듈, 패키지

모듈: 변수, 함수, 클래스 등을 포함하고 있는 하나의 파이썬 파일.

패키지: 모듈들의 집합체. 서로 관련 있는 모듈들이 디렉터리 구조 안에 모여 있는 것.

## 모듈

```python
# my_math.py
PI = 3.14


class Calculator:
    @staticmethod
    def add(num1, num2):
        return num1 + num2

    @staticmethod
    def subtract(num1, num2):
        return num1 - num2

    @staticmethod
    def product(num1, num2):
        return num1 * num2

    @staticmethod
    def divide(num1, num2):
        return num1 / num2


def calc_circle_area(radius):
    return PI * (radius ** 2)
```

위와 같은 파일 my_math.py가 모듈.

모듈이 같은 디렉터리 안에 있으면 다음과 같이 import해서 사용할 수 있음.

```python
import my_math

radius = 5
circle_area = my_math.calc_circle_area(radius)
print(f"반지름 5인 원의 넓이는 {circle_area}입니다.")

result1 = my_math.Calculator.add(5, 7)
print(result1)

result2 = my_math.Calculator.divide(12, 3)
print(result2)
```

## 패키지

```zsh
sports/
    __init__.py
    soccer/
        __init__.py
        epl.py
        k_league.py
    baseball/
        __init__.py
        kbo.py
        mlb.py
    basketball/
        __init__.py
        nba.py
        kbl.py
```

`__init__.py` 파일은 해당 디렉터리가 패키지의 일부임을 나타냄. python 3.3 버전부터는 없어도 됨.

```python
from sports.soccer import epl

epl.show_epl()
```
