# 예외 처리

예외(오류)가 발생했을 때 프로그램이 종료되지 않도록 처리해주는 기법.

경우에 따라서는 일부러 예외가 발생하게 하기도 함.

## 예외 종류

참고자료: <https://docs.python.org/3/library/exceptions.html#bltin-exceptions>

- AssertionError: assert문이 실패할 때 발생

    ```python
    assert 3 + 5 == 8
    assert 3 + 5 == 7 # AssertionError
    ```

    참고자료: <https://www.geeksforgeeks.org/python-assertion-error/>

- AttributeError: 존재하지 않는 속성에 접근하려고 할 때 발생

    ```python
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age


    p1 = Person('홍길동', 29)
    print(p1.job) # AttributeError: 'Person' object has no attribute 'job'
    ```

- EOFError
- FloatingPointError
- GeneratorExit
- ImportError: 모듈을 load 하려고 하는데 문제가 있을 때 발생

    ```python
    from time import sleep
    from time import wake # ImportError: cannot import name 'wake' from 'time' (unknown location)
    ```

- ModuleNotFoundError: 모듈이 설치되어 있지 않은 경우 발생

    ```python
    import numpy # ModuleNotFoundError: No module named 'numpy'
    ```

- IndexError: 인덱스 오류

    ```python
    a = [1, 2, 3, 4, 5]

    print(a[6]) # IndexError: list index out of range
    ```

- KeyError: 딕셔너리에서 존재하지 않는 키에 접근할 때 발생

    ```python
    a = {'name': '심교훈', 'age': 35}

    print(a['hobby']) # KeyError: 'hobby'
    ```

- KeyboardInterrupt: 사용자가 프로그램을 중단시키고자 Ctrl + C와 같은 신호를 보냈을 때 발생

    ```python
    while True:
        print("무한반복")

    # KeyboardInterrupt
    ```

- MemoryError
- NameError: 정의되지 않은 변수나 함수를 참조하려고 할 때 발생

    ```python
    a = 5

    print(b) # NameError: name 'b' is not defined
    ```

- NotImplementedError
- OSError
- FileNotFoundError: 파일을 못 찾을 때 발생

    ```python
    with open('test.txt', 'r') as File: # FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'
        print(File.readlines())
    ```

- OverflowError: 산술 연산의 결과가 표현하기에 너무 클 때 발생

    ```python
    1.0 / (10**500) # OverflowError: int too large to convert to float
    ```

- RecursionError
- ReferenceError
- RuntimeError
- StopIteration: 이터레이터가 더이상 순회할 것이 없을 때 발생

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

- StopAsyncIteration
- SyntaxError: 구문 오류, 파이썬 문법을 지키지 않았을 때 발생

    ```python
    for i in range(5)
        print(i)

    # SyntaxError: expected ':'
    ```

- IndentationError: 들여쓰기 오류

    ```python
    for i in range(5):
    print(i)

    # IndentationError: expected an indented block after 'for' statement on line 1
    ```

- TabError
- SystemError
- SystemExit
- TypeError: 적절하지 않은 타입의 객체에 함수 등이 적용되었을 때 발생

    ```python
    a = 5
    b = '바나나'
    print(a + b) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
    ```

- UnboundLocalError
- UnicodeError
- UnicodeEncodeError
- UnicodeDecodeError
- UnicodeTranslateError
- ValueError: 값 오류

    ```python
    a = int("7.23") # ValueError: invalid literal for int() with base 10: '7.23'
    ```

- ZeroDivisionError: 어떤 숫자를 0으로 나누려고 할 때 발생

    ```python
    a = 5/0 # ZeroDivisionError: division by zero
    ```

- EnvironmentError
- IOError
- WindowsError

### Exception 계층 구조

```txt
BaseException
 ├── BaseExceptionGroup
 ├── GeneratorExit
 ├── KeyboardInterrupt
 ├── SystemExit
 └── Exception
      ├── ArithmeticError
      │    ├── FloatingPointError
      │    ├── OverflowError
      │    └── ZeroDivisionError
      ├── AssertionError
      ├── AttributeError
      ├── BufferError
      ├── EOFError
      ├── ExceptionGroup [BaseExceptionGroup]
      ├── ImportError
      │    └── ModuleNotFoundError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── MemoryError
      ├── NameError
      │    └── UnboundLocalError
      ├── OSError
      │    ├── BlockingIOError
      │    ├── ChildProcessError
      │    ├── ConnectionError
      │    │    ├── BrokenPipeError
      │    │    ├── ConnectionAbortedError
      │    │    ├── ConnectionRefusedError
      │    │    └── ConnectionResetError
      │    ├── FileExistsError
      │    ├── FileNotFoundError
      │    ├── InterruptedError
      │    ├── IsADirectoryError
      │    ├── NotADirectoryError
      │    ├── PermissionError
      │    ├── ProcessLookupError
      │    └── TimeoutError
      ├── ReferenceError
      ├── RuntimeError
      │    ├── NotImplementedError
      │    └── RecursionError
      ├── StopAsyncIteration
      ├── StopIteration
      ├── SyntaxError
      │    └── IndentationError
      │         └── TabError
      ├── SystemError
      ├── TypeError
      ├── ValueError
      │    └── UnicodeError
      │         ├── UnicodeDecodeError
      │         ├── UnicodeEncodeError
      │         └── UnicodeTranslateError
      └── Warning
           ├── BytesWarning
           ├── DeprecationWarning
           ├── EncodingWarning
           ├── FutureWarning
           ├── ImportWarning
           ├── PendingDeprecationWarning
           ├── ResourceWarning
           ├── RuntimeWarning
           ├── SyntaxWarning
           ├── UnicodeWarning
           └── UserWarning
```

## try, except

try 문 안에서 예외가 발생하면 프로그램을 종료하지 않고 except 문의 코드를 실행.

```python
a = [1, 2, 3, 4, 5]
print(a[6]) # IndexError: list index out of range
print("프로그램 종료") # 실행되지 않음   
```

위 코드를 실행하면 두번째 행에서 예외가 발생하면서 마지막 행이 싪행되지 않음.

프로그램이 원치 않게 종료되는 것은 치명적인 일. 예외 처리를 해주면 종료되지 않고 계속 작동할 수 있게 하는 것이 가능.

```python
a = [1, 2, 3, 4, 5]

try:
    print(a[6])
except:
    print("프로그램 종료 안 되고 계속 실행") # 프로그램 종료 안 되고 계속 실행

print("프로그램 종료") # 프로그램 종료
```

## 예외 발생시키기

때로는 일부러 예외를 발생시키곤 한다.

예외를 발생시킬 때는 raise 라는 예약어를 사용.

```python
def my_function1():
    print("나만의 함수1입니다.")

def my_function2():
    raise NotImplementedError

my_function1() # 나만의 함수1입니다.
my_function2() # NotImplementedError
```

NotImplementedError는 아직 작성하지 않은 함수 등을 호출했을 때 발생시키는 예외.

## 커스텀 예외 만들기

프로그램의 필요에 따라 Exception 클래스를 상속 받아 나만의 예외를 만들 수 있다.

```python
class KyohoonException(Exception):
    pass


def check_name(name):
    if name == "교훈":
        raise KyohoonException()
    print(name)

check_name('준혁') # 준혁
check_name('교훈') # KyohoonException
```
