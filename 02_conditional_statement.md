# 조건문

프로그램에 어떠한 논리를 줄 때 필요한 문법.

만약 ~면 ~하고, 그게 아니면 ~해.

## if, elif, else

```python
if 불 값을 반환해주는 표현식:
    위 조건이 참일 때 실행할 코드
elif 불 값을 반환해주는 표현식:
    위 조건이 참일 때 실행할 코드
else:
    모든 조건이 참이 아닐 때 실행할 코드  
```

input() 함수: 사용자로부터 어떠한 값을 입력받고자 할 때 사용. 입력받는 것은 항상 문자열로 판단.

```python
age = int(input("당신의 나이를 입력하세요>>"))

if 10 <= age < 20:
    print("10대입니다")
elif 20 <= age < 30:
    print("20대입니다")
elif 30 <= age < 40:
    print("30대입니다")
else:
    print("10대, 20대, 30대가 아닙니다") 
```

---

## 논리 연산자

- and: 그리고
- or: 또는
- not: 아니다

### and

결혼정보업체: 연봉이 6000 이상이고, 키가 180 이상이면 A 등급을 주자.

```python
annual_salary = int(input("당신의 연봉을 입력하세요(4000만원이라면 4000으로 입력할 것)>>"))
height = int(input("당신의 키를 입력하세요(172cm라면 172로 입력할 것)>>"))

if annual_salary >= 6000 and height >= 180:
    print("당신은 A급 신랑감입니다.")
else:
    print("당신은 A급 신랑감이 아닙니다.")
```

### or

결혼정보업체: 연봉이 6000 이상이거나, 키가 180 이상이면 A 등급을 주자.

```python
annual_salary = int(input("당신의 연봉을 입력하세요(4000만원이라면 4000으로 입력할 것)>>"))
height = int(input("당신의 키를 입력하세요(172cm라면 172로 입력할 것)>>"))

if annual_salary >= 6000 or height >= 180:
    print("당신은 A급 신랑감입니다.")
else:
    print("당신은 A급 신랑감이 아닙니다.")
```

### not

결혼정보업체: 사람의 성씨가 김씨가 아니면 A급을 주자. (예를 들어, 어떤 여성이 김씨 성을 가진 남자에게 매우 디였다면...)

```python
name = input("당신의 이름을 입력하세요>>")

if not (name[0] == "김"):
    print("당신은 A급 신랑감입니다.")
else:
    print("당신은 A급 신랑감이 아닙니다.")
```

---

## 조건문 실습

사용자가 3 또는 4 또는 5를 입력하면 "봄"이라고 출력하고, 6 또는 7 또는 8을 입력하면 "여름"이라고 출력하고, 9 뚀는 10 또는 11을 입력하면 "가을"이라고 출력하고, 12 또는 1 또는 2를 입력하면 "겨울"이라고 출력하는 프로그램을 만드시오.

그 외의 숫자를 입력하면 "잘못된 입력"을 출력할 것!

input() 함수와 if 문을 사용할 것!