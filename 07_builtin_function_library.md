# 내장 함수, 표준 라이브러리, 외부 라이브러리

## 내장 함수 (Built-in Functions)

내장 함수: 개발의 편이를 위해 기본적으로 제공하고 있는 함수들.

주요한 내장 함수는 외우고 있어야 코딩 테스트를 잘 볼 수 있음.

### 내장 함수 목록

참고자료: <https://docs.python.org/3/library/functions.html>

- abs(): 절대값

    ```python
    print(abs(-3.14)) # 3.14
    ```

- aiter(): async iterator 반환, 파이썬 3.10에서 추가
- all(): iterable의 모든 요소가 True일 때 True를 반환

    ```python
    a = [1, 2, 3, 4, 5]
    print(all(a)) # True

    b = [1, 2, 0, 4, 5]
    print(all(b)) # False

    c = [True, True, True]
    print(all(c)) # True

    d = [True, False, True]
    print(all(d)) # False
    ```

- any(): iterable의 어떤 요소라도 True면 True를 반환

    ```python
    a = [1, 2, 3, 4, 5]
    print(any(a)) # True

    b = [0, 0, 0, 4, 0]
    print(any(b)) # True

    c = [False, False, False]
    print(any(c)) # False

    d = [True, False, True]
    print(any(d)) # True
    ```

- anext()
- ascii()
- bin(): 정수를 0b로 시작하는 이진수로 변환

    ```python
    print(bin(4)) # 0b100
    print(bin(10)) # 0b1010
    print(bin(255)) # 0b11111111
    ```

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
- dir(): 어떤 객체가 갖고 있는 메소드 및 속성 목록을 확인하고 싶을 때

    ```python
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def introduce(self):
            print(f"저는 {self.age}살, {self.name}입니다.")


    p1 = Person('홍길동', 19)
    print(dir(p1)) # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'introduce', 'name']
    ```

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
- help(): 객체 사용법 확인

    ```python

    ```

- hex(): 정수를 0x로 시작하는 16진수로 변환

    ```python
    print(hex(10)) # 0xa
    print(hex(17)) # 0x11
    print(hex(255)) # 0xff
    print(hex(256)) # 0x100
    ```

- id(): 어떤 객체의 주소값 확인
- input(): 사용자로부터 문자열 입력받을 때 사용
- int(): 정수로 변환이 가능한 문자열을 숫자로 변환

    ```python
    a = "13" 
    print(type(a)) # <class 'str'>
    
    b = int(a)
    print(b) # 13
    print(type(b)) # <class 'int'>
    ```

- isinstance(): 객체가 특정 클래스의 인스턴스인지 확인할 때 사용
- issubclass()
- iter(): iterator 객체 반환
- len(): 리스트 요소의 개수 또는 문자열의 길이 등을 반환

    ```python
    print(len("심교훈")) # 3
    print(len("python")) # 6 
    print(len([1, 2, 3, 4, 5])) # 5
    ```

- list(): 리스트 생성시 사용
- locals()
- map(): 이터러블의 모든 요소를 특정 타입으로 변환하고자 할 때 사용

    ```python
    a = [1, 2, 3, 4, 5]
    b = list(map(str, a))
    print(b) # ['1', '2', '3', '4', '5']
    ```

- max(): 최대값

    ```python
    print(max(1, 4, 3)) # 4
    print(max([1, 7, 4, 2, 6])) # 7
    ```

- memoryview()
- min(): 최소값

    ```python
    print(min(5, 2, 7)) # 2
    print(min([1, 2, 3, -2, 6])) # -2
    ```

- next(): 이터레이터가 다음 요소 검색
- object()
- oct(): 정수를 0o로 시작하는 8진수로 변환
- open()
- ord()
- pow(): 거듭제곱

    ```python
    print(pow(2, 3)) # 8
    print(pow(5, 2)) # 25
    ```

- print(): 콘솔에 문자열 등 출력
- property()
- range(): 반복문 등에서 유용하게 쓰이는 range 객체 생성
- repr(): 객체의 출력가능한 표현을 담은 문자열을 반환

    ```python
    ```

- reversed()
- round(): 반올림

    ```python
    print(round(3.14)) # 3
    print(round(3.14, 1)) # 3.1
    ```

- set(): set 생성시 사용
- setattr()
- slice()
- sorted()
- staticmethod(): 정적 메서드 선언시 사용
- str(): 문자열로 변환하고 싶을 때 사용

    ```python
    a = str(12)

    print(a) # 12
    print(type(a)) # <class 'str'>
    ```

- sum(): 리스트와 같은 iterable의 요소들의 합
- super()
- tuple(): 튜플 생성시 사용
- type(): 객체의 자료형 알고 싶을 때 사용
- vars()
- zip()
- __import__()

### 참고: iterable과 iterator

리스트, 튜플 등과 같이 요소를 하나씩 순회할 수 있는 객체를 iterable이라고 함.

반면 iterator는 순서대로 다음 값을 리턴할 수 있는 객체.

`__next__` 메소드로 다음 값을 반환할 수 있으면 iterator, 그렇지 않으면 iterable.

```python
a = [1, 2, 3, 4, 5]
iterator_a = iter(a)

print(type(a)) # <class 'list'>
print(type(iterator_a)) # <class 'list_iterator'>

print(dir(a)) # ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
print(dir(iterator_a)) # ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__length_hint__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__']
```

위 예제에서 볼 수 있듯이 iterable 객체에는 __next__ 메소드가 없고, iterator 객체에는 __next__ 메소드가 있음.

```python
a = [1, 2, 3, 4, 5]
iterator_a = iter(a)

print(next(iterator_a)) # 1
print(next(iterator_a)) # 2
print(next(iterator_a)) # 3
print(next(iterator_a)) # 4
print(next(iterator_a)) # 5
print(next(iterator_a)) # StopIteration
```

---

## 표준 라이브러리

파이썬 설치시 기본으로 제공되는 라이브러리.

ex) random, sys, os, time, datetime, logging 등

각 라이브러리 별로 사용법이 다 다름. 자주 쓰는 라이브러리 사용법은 잘 알아두는 것이 좋음.

---

## 외부 라이브러리

표준으로 제공되지 않기 때문에 개발자가 별도로 설치해서 사용하는 라이브러리.

ex) pandas, opencv-python, requests, fastapi, numpy, matplotlib, qrcode 등

## pip 명령어 정리

pip는 파이썬의 패키지 관리자

- 패키지 목록 확인: `pip list`

- 패키지 설치: `pip install [패키지명]`

- 패키지 삭제: `pip uninstall [패키지명]`

## qrcode 라이브러리로 내 블로그 또는 깃허브 QR 코드 만들어보기

패키지 설치

- `pip install qrcode`
- `pip install pillow`

아래 파이썬 코드를 실행하면 현재 작업 디렉토리에 my_qrcode.png라는 이름의 이미지 파일이 생성될 것임. 열어보면 QR 코드가 담겨 있을 것임.

```python
import qrcode

url = 'https://bskyvision.com'
qrcode_img = qrcode.make(url)
qrcode_img.save('./my_qrcode.png')
```
