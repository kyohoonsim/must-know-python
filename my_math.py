PI = 3.14


class Calculator:
    @staticmethod
    def add(num1, num2):
        return num1 + num2

    @staticmethod
    def subtract(num1, num2):
        return num1 - num2

    @staticmethod
    def product(num1, num2):
        return num1 * num2

    @staticmethod
    def divide(num1, num2):
        return num1 / num2


def calc_circle_area(radius):
    return PI * (radius ** 2)