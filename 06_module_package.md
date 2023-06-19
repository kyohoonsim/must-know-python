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


def circle_area(radius):
    return PI * (radius ** 2)
```

위와 같은 파일 my_math.py가 모듈.

모듈이 같은 디렉터리 안에 있으면 다음과 같이 import해서 사용할 수 있음.

```python

```

## 패키지
