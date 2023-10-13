def calc_avg(H: int, AB: int) -> float:
    """타율을 구합니다

    Args:
        H (int): 안타 개수
        AB (int): 타수

    Returns:
        float: 타율 (소수점 4번째 자리에서 반올림)

    Raises:
        TypeError: H와 AB는 모두 정수여야 합니다
    """
    if not (isinstance(H, int) and isinstance(AB, int)):
        raise TypeError("H와 AB는 모두 정수여야 합니다")

    return round(H / AB, 3)


print("타율: ", calc_avg(125, 334))  # 타율:  0.374
print("타율: ", calc_avg(199, 641))  # 타율:  0.31
print("타율: ", calc_avg(125.2, 334))  # TypeError: H와 AB는 모두 정수여야 합니다
