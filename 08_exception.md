# 예외 처리

예외(오류)가 발생했을 때 프로그램이 종료되지 않도록 처리해주는 기법.

경우에 따라서는 일부러 예외가 발생하게 하기도 함.

## 예외 종류

참고자료: <https://docs.python.org/3/library/exceptions.html#bltin-exceptions>

- AssertionError
- AttributeError
- EOFError
- FloatingPointError
- GeneratorExit
- ImportError
- ModuleNotFoundError
- IndexError
- KeyError
- KeyboardInterrupt
- MemoryError
- NameError
- NotImplementedError
- OSError
- OverflowError
- RecursionError
- ReferenceError
- RuntimeError
- StopIteration
- StopAsyncIteration
- SyntaxError
- IndentationError
- TabError
- SystemError
- SystemExit
- TypeError
- UnboundLocalError
- UnicodeError
- UnicodeEncodeError
- UnicodeDecodeError
- UnicodeTranslateError
- ValueError
- ZeroDivisionError
- EnvironmentError
- IOError
- WindowsError

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