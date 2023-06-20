class KyohoonException(Exception):
    pass
    # def __str__(self):
    #     return "교훈이란 이름입니다."


def check_name(name):
    if name == "교훈":
        raise KyohoonException("교훈 예외 발생")
    print(name)

check_name('준혁')
check_name('교훈')