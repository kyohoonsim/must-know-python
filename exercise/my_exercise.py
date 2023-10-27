class NotAllowedNameException(Exception):
    pass


def check_name(name):
    if name == "교훈":
        raise NotAllowedNameException()
    print(name)

check_name('준혁') # 준혁
check_name('교훈') # NotAllowedNameException