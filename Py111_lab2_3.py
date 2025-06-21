def factorial_recursive(n: int) -> int:
    """
    Рассчитать факториал числа n рекурсивным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)

print(factorial_recursive(5))
