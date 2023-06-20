# 내장 함수, 표준 라이브러리, 외부 라이브러리

## 내장 함수 (Built-in Functions)

내장 함수: 개발의 편이를 위해 기본적으로 제공하고 있는 함수들.

### 내장 함수 목록

참고자료: <https://docs.python.org/3/library/functions.html>

- abs(): 절대값
- aiter()
- all()
- any()
- anext()
- ascii()
- bin()
- bool()
- breakpoint()
- bytearray()
- bytes()
- callable()
- chr()
- classmethod(): 클래스 메서드 선언시 사용
- compile()
- complex()
- delattr()
- dict(): dictionary 생성시 사용
- dir()
- divmod()
- enumerate()
- eval()
- exec()
- filter()
- float()
- format()
- frozenset()
- getattr()
- globals()
- hasattr()
- hash()
- help()
- hex()
- id()
- input()
- int(): 정수로 변환하고 싶을 때 사용
- isinstance(): 객체가 특정 클래스의 인스턴스인지 확인할 때 사용
- issubclass()
- iter()
- len(): 리스트 요소의 개수 또는 문자열의 길이 등을 반환
- list(): 리스트 생성시 사용
- locals()
- map()
- max()
- memoryview()
- min()
- next()
- object()
- oct()
- open()
- ord()
- pow()
- print()
- property()
- range()
- repr()
- reversed()
- round()
- set(): set 생성시 사용
- setattr()
- slice()
- sorted()
- staticmethod(): 정적 메서드 선언시 사용
- str(): 문자열로 변환하고 싶을 때 사용
- sum()
- super()
- tuple(): 튜플 생성시 사용
- type(): 객체의 자료형 알고 싶을 때 사용
- vars()
- zip()
- __import__()

---

## 표준 라이브러리

파이썬 설치시 기본으로 제공되는 라이브러리.

ex) random, sys, os, time, datetime, logging 등

---

## 외부 라이브러리

pip install [패키지명] 등의 방식으로 설치해서 사용하는 라이브러리.

ex) pandas, opencv-python, requests, fastapi, numpy, matplotlib 등