def say_hello(name1: str, name2: str) -> None:
    """인사 함수

    Args:
        name1 (str): 인사하는 사람 이름
        name2 (str): 인사받는 사람 이름

    Returns:
        None

    Raises:
        None
    """
    print(f"{name1}이 {name2}에게 인사를 합니다")


say_hello('교훈', '준혁')
say_hello('준혁', '수호')
say_hello('수호', '교훈')
