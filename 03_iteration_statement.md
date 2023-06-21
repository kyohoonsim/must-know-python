# 반복문

어떤 작업을 반복해서 수행하고 싶을 때 사용.

## while

```python
while True:
    print("무한반복")
```

무한 반복 멈추려면, Ctrl + C

```python
cnt = 0

while cnt < 10:
    cnt += 1
    print(cnt)
```

---

## for

리스트, 튜플 등에 있는 요소들을 하나씩 꺼내서 사용할 수 있음

```python
fruit = ['banana', 'apple', 'cherry']

for item in fruit:
    print(item)
```

### enumerate() 함수

인덱스 값과 함께 반환

```python
fruit = ['banana', 'apple', 'cherry']

for idx, item in enumerate(fruit):
    print(idx, item)
```

### zip() 함수

두 개 이상의 이터러블을 함께 이터레이션하고 싶을 때

```python
fruit = ['banana', 'apple', 'cherry']
name = ['심교훈', '도준혁', '박수호']

for item1, item2 in zip(fruit, name):
    print(item1, item2)
```

### range() 함수

```python
for i in range(10):
    print(i)

for i in range(1, 11):
    print(i)

for i in range(0, 11, 2):
    print(i)
```

---

## break

반복문에서 iteration이 되는 도중에 탈출이 필요한 경우에 사용

```python
people = ['심교훈', '도준혁', '조두순', '박수호']

for person in people:
    if person == '조두순':
        print(f"위험 인물 {person}이 접근했습니다. 파티를 중단합니다.") 
        break    

    print(f"{person}님 출입 가능!")
```

---

## continue

반복문에서 어떤 조건을 만족했을 때 아래 코드는 실행하지 않고 다시 반복문 처음으로 돌아가서 iteration 수행

```python
people = ['심교훈', '도준혁', '조두순', '박수호']

black_list = ['조두순', '신창원']

members = []

for person in people:
    if person in black_list:
        print(f"위험 인물 {person}이 접근했습니다. {person}은 출입이 불가합니다.") 
        continue

    print(f"{person}님 출입 가능!")
    members.append(person)

print("파티 출입 인물: ", members)
```

---

## 반복문 실습

주인의 명령에 따라 강아지를 돌보는 로봇을 프로그래밍해보자. 사용자가 1을 누르면, "먹이 주기"가 콘솔에 출력되게 한다. 프로그램은 종료되지 않은 상태에서 다음 명령을 기다린다. 사용자가 2를 누르면, "놀아 주기"가 콘솔에 출력된다. 사용자가 3을 누르면, "산책 하기", 4를 누르면 "목욕 시키기"가 출력된다. 사용자가 q를 누를 때까지 이 프로그램은 종료하지 않는다. 최대한 예쁘게 만들어볼 것.