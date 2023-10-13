def add(num1: int, num2: int) -> int:
    '''매개변수로 전달받은 두 개의 정수를 더해서 반환

    Args:
        num1 (int): 첫번째 정수
        num2 (int): 두번째 정수

    Returns:
        int: 전달받은 두 개의 정수의 합, num1 + num2
    
    Raises:
        TypeError: num1 또는 num2가 정수가 아닙니다
    '''
    if not (isinstance(num1, int) and isinstance(num2, int)):
        raise TypeError("num1 또는 num2가 정수가 아닙니다.")

    return num1 + num2


print(add(1, 5))  # 6
print(add("2", 3))  # TypeError: num1 또는 num2가 정수가 아닙니다.
