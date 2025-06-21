from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """

    if not container:
        return []

    max_value = max(container)

    count = [0] * (max_value + 1)

    for elem in container:
        count[elem] += 1

    sorted_container = []
    for elem in range(len(count)):
        sorted_container.extend([elem] * count[elem])

    return sorted_container

    # TODO реализовать алгоритм сортировки подсчетами

