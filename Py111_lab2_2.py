def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    if n < 0:
        raise ValueError("Факториал отрицательного цисла не может быть найден")
    if not isinstance(n, int):
        raise TypeError("Только целое число")

    
    fact_n = 1
    for i in range(1, n+1):
        fact_n *= i
    return fact_n# TODO реализовать итеративный алгоритм нахождения факториала
