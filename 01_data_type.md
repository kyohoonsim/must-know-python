# 자료형 (data type)

코딩은 결국 어떠한 자료, 데이터를 다루기 위한 기술.

숫자, 문자열 등과 같은 자료(data)의 형태를 자료형(data type)이라고 함.

따라서 자료형을 잘 알아야 코딩을 잘 할 수 있음.

## 대표적인 자료형들

- 숫자
- 문자열
- 불(boolean)
- 리스트
- 튜플
- 딕셔너리
- 집합

자료형을 확인하는 함수: type()

---

## 숫자

말 그대로 숫자 형태의 자료형.

### 산술 연산자

- `+` : 더하기
- `-` : 빼기
- `*` : 곱하기
- `/` : 나누기
- `%` : 나머지

    ```python
    print(17 % 5) # 2
    ```

- `//` : 몫

    ```python
    print(17 % 5) # 3
    ```

- `**` : 거듭제곱

    ```python
    print(2 ** 5) # 32
    ```

---

## 문자열

말 그대로 문자, 단어, 글 형태의 자료형.

### 문자열을 만드는 다양한 방법

- `'문자열'`
- `"문자열"`
- `'''문자열'''`
- `"""문자열"""`

문자열 안에 따옴표를 넣고 싶다면?

```python
print('"안녕?"이라고 그녀가 말했다') # "안녕?"이라고 그녀가 말했다
print("'안녕?'이라고 나는 마음 속으로 말했다.") # '안녕?'이라고 나는 마음 속으로 말했다.
```

### 문자열 연산

- 문자열 + 문자열: 문자열 합치기

    ```python
    a = "사과"
    b = "딸기"
    print(a + b) # 사과딸기
    ```

- 문자열 * 숫자: 문자열 반복

    ```python
    print("bye"*3) # byebyebye
    print("="*5) # *****

    print("="*40)
    print("가계부 프로그램")
    print("="*40)

    '''
    ========================================
    가계부 프로그램
    ========================================
    '''
    ```

### 인덱싱 (indexing)

문자열 중 문자 하나를 가리킴.

파이썬에서 인덱스는 0부터 시작.

```python
name = '심교훈'

print(name[0]) # 심
print(name[1]) # 교
print(name[2]) # 훈
```

### 슬라이싱 (slicing)

문자열의 일부를 잘라냄.

```python
title = "범죄도시3"

print(title[0:2]) # 범죄
print(title[0:3]) # 범죄도
print(title[2:4]) # 도시
```

### f-string 포매팅

문자열 안에 어떠한 데이터를 넣을 때 유용.

파이썬 3.6 이상 사용 가능.

```python
name = "심교훈"
age = 19

print(f"제 이름은 {name}이고, 나이는 {age}입니다.") # 제 이름은 심교훈이고, 나이는 19입니다.
```

어떤 숫자를 소수점 2자리까지 출력하고 싶은 경우

```python
PI = 3.141592

print(f"파이: {PI:.2f}") # 파이: 3.14
```

어떤 숫자를 총 10칸을 차지하면서 소수점 2자리까지 출력하고 싶은 경우

```python
PI = 3.141592

print(f"파이: {PI:10.2f}") # 파이:       3.14
```

참고자료: <https://bskyvision.com/entry/python-%EB%AC%B8%EC%9E%90%EC%97%B4-%ED%8F%AC%EB%A7%B7%ED%8C%85-%EB%B0%A9%EB%B2%95%EB%93%A4-%EC%A0%95%EB%A6%AC>

### 문자열 주요 메소드

문자열도 객체이기 때문에 메소드라는 것이 존재.

- count(): 특정 문자 개수 세기

    ```python
    a = "banana"

    print(a.count("a")) # 3
    print(a.count("n")) # 2
    ```

- upper(): 소문자를 대문자로 변환

    ```python
    print("My name is Kyohoon Sim.".upper()) # MY NAME IS KYOHOON SIM.
    ```

- lower(): 대문자를 소문자로 변환

    ```python
    print("My name is Kyohoon Sim.".lower()) # my name is kyohoon sim.
    ```

- strip(): 양옆 공백 제거

    ```python
    print("  Hello World    ".strip()) # Hello World
    ```

- split(): 문자열 특정 문자 기준으로 분할하여 리스트에 담음.

    ```python
    a = "My  name  is  kyohoon  sim."
    b = a.split(" ")
    print(b) # ['My', 'name', 'is', 'kyohoon', 'sim.']
    ```

문자열은 이보다 많은 메소드를 가지고 있음. 그 전체 목록을 확인하고 싶을 때는 dir(객체)로 확인 가능.

```python
name = '심교훈'
print(type(name)) # <class 'str'>
print(dir(name)) # ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

---

## 불 (Boolean)

True (참), False (거짓)을 나타내는 자료형

반복문, 조건문 등에서 많이 사용됨.

---

## 리스트 (list)

여러 개의 요소를 담기 위한 자료형

대괄호 [] 로 요소들을 감싸줌.

```python
a = [1, 2, 3, 4, 5]

fruit = ["banana", "apple", "strawberry", "watermelon"]

b = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
```

리스트의 요소로 리스트를 담을 수도 있음.

### 인덱싱

리스트의 특정 요소를 가리킴.

```python
fruit = ["banana", "apple", "strawberry", "watermelon"]

print(fruit[0]) # banana
print(fruit[2]) # strawberry
print(fruit[-1]) # watermelon

fruit[0] = "peer"
print(fruit) # ['peer', 'apple', 'strawberry', 'watermelon']
```

### 슬라이싱

리스트의 일부를 잘라냄.

```python
a = [1, 2, 3, 4, 5, 6, 7, 8]

print(a[0:4]) # [1, 2, 3, 4]
print(a[2:5]) # [3, 4, 5]
print(a[:3]) # [1, 2, 3]
print(a[5:]) # [6, 7, 8]
```

### 리스트 주요 메소드

- append(): 리스트에 요소 추가

    ```python
    a = [1, 2, 3, 4, 5]

    a.append(6)

    print(a) # [1, 2, 3, 4, 5, 6]
    ```

- pop(): 리스트 마지막 요소 반환 및 제거

    ```python
    a = [1, 2, 3, 4, 5]
    
    print(a.pop())
    print(a)
    ```

- sort(): 리스트 요소 정렬

    ```python
    a = [1, 5, 4, 2, 3]
    a.sort()
    print(a) # [1, 2, 3, 4, 5]

    b = [10, 20, 50, 30, 40]
    b.sort(reverse=True)
    print(b) # [50, 40, 30, 20, 10]
    ```

- reverse(): 리스트 요소 순서 뒤집기

    ```python
    a = [1, 2, 3, 4, 5]
    
    a.reverse()
    print(a) # [5, 4, 3, 2, 1]
    ```

- index(): 특정 요소의 인덱스 반환

    ```python
    fruit = ["banana", "apple", "strawberry", "watermelon"]

    print(fruit.index("apple")) # 1
    print(fruit.index("strawberry")) # 2
    ```

---

## 튜플 (tuple)

여러 개의 요소를 담기 위한 자료형

소괄호 () 로 요소들을 감싸줌.

리스트와 마찬가지로 인덱싱, 슬라이싱 가능.

### 리스트와의 차이

- 값 변경 불가능 (immutable), 리스트는 변경 가능 (mutable)

    ```python
    a = (1, 2, 3)

    print(a[0]) # 1
    
    a[0] = 4 # TypeError: 'tuple' object does not support item assignment
    ```

---

## 딕셔너리 (dictionary)

키(key)-값(value)의 관계로 여러 개의 데이터를 담기 위한 자료형

중괄호 {} 로 키:값 형태의 요소들을 감싸줌.

인덱스 대신 키로 데이터 접근

```python
fruit = {"banana":5, "strawberry":20, "apple":7}

print(fruit["banana"]) # 5
print(fruit["apple"]) # 7 

print(fruit[0]) # KeyError: 0
```

### 딕셔너리에 키:값 쌍 추가하는 방법

```python
fruit = {"banana":5, "strawberry":20, "apple":7}

fruit["orange"] = 12
print(fruit) # {'banana': 5, 'strawberry': 20, 'apple': 7, 'orange': 12}
```

### 딕셔너리 주요 메소드

- keys(): 키만 추출하여 반환.

    ```python
    fruit = {"banana":5, "strawberry":20, "apple":7}

    print(fruit.keys()) # dict_keys(['banana', 'strawberry', 'apple'])
    ```

- values(): 값만 추출하여 반환.

    ```python
    fruit = {"banana":5, "strawberry":20, "apple":7}

    print(fruit.values()) # dict_values([5, 20, 7])
    ```

- items(): 키와 값을 튜플로 묶어서 dict_items 객체로 반환.

    ```python
    fruit = {"banana":5, "strawberry":20, "apple":7}

    print(fruit.items()) # dict_items([('banana', 5), ('strawberry', 20), ('apple', 7)])
    ```

- get(): 키로 선택한 요소의 값 반환. 없는 키일 경우 None 반환.

    ```python
    fruit = {"banana":5, "strawberry":20, "apple":7}

    print(fruit.get("banana")) # 5
    print(fruit.get("cherry")) # None
    print(fruit["cherry"]) # KeyError: 'cherry'
    ```

- setdefault(): 키로 선택한 요소의 값 반환. 없는 키일 경우 default로 설정해 준 값으로 키-값 쌍 추가.

    ```python
    fruit = {"banana":5, "strawberry":20, "apple":7}

    print(fruit.setdefault('banana', 0)) # 5
    print(fruit.setdefault('cherry', 0)) # 0
    print(fruit) # {'banana': 5, 'strawberry': 20, 'apple': 7, 'cherry': 0}
    ```

- pop(): 키로 선택한 요소의 값 반환하면서 삭제.

    ```python
    fruit = {"banana":5, "strawberry":20, "apple":7}

    print(fruit.pop("banana")) # 5
    print(fruit) # {'strawberry': 20, 'apple': 7}
    ```

---

## 집합 (set)

중괄호 {}로 요소들을 감싸줌.

중복된 값을 허용하지 않음.

```python
a = {1, 2, 3}
print(a) # {1, 2, 3}

b = {1, 2, 2, 3, 3, 3}
print(b) # {1, 2, 3}
```

인덱싱 불가능.

### 집합 연산자

- 합집합: a | b

- 교집합: a & b

- 차집합: a - b

- 대칭차집합: a ^ b, 교집합을 제외한 나머지

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b) # {1, 2, 3, 4, 5, 6}
print(a & b) # {3, 4}
print(a - b) # {1, 2}
print(a ^ b) # {1, 2, 5, 6}
```

### set 주요 메소드

- add(): 1개 값 추가

    ```python
    a = {1, 2, 3}

    a.add(4)
    print(a) # {1, 2, 3, 4} 
    ```

- update(): 여러 개 값 추가

    ```python
    a = {1, 2, 3}

    a.update([4, 5, 6])
    print(a) # {1, 2, 3, 4, 5, 6} 
    ```

- remove(): 특정 값 제거

    ```python
    a = {1, 2, 3}

    a.remove(2)
    print(a) # {1, 3}
    ```

---

## 자료형 실습

"i Am a boY"라는 문자열을 문자열 객체의 어떤 메서드를 사용하여 "I am a boy"로 변환해서 콘솔에 출력할 것.
