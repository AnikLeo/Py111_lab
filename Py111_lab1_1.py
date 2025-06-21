"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        """
        Очередь с помощью python list

        """
        self._len=0
        self._list=[]

    def enqueue(self, elem: Any) -> None:
        """
        Добавление элемент в конец очереди

        :param elem: Элемент, который должен быть добавлен
        """
        self._len += 0
        self._list.append(elem)

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        if not self._list:
            raise IndexError

        self._len -= 0
        return self._list.pop(0)

    def peek(self, ind: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        if not isinstance(ind, int):
            raise TypeError
        if not 0<= ind <= len(self._list):
            raise IndexError

        return self._list[ind]

    def clear(self) -> None:
        """ Очистка очереди. """
        self._len=0
        self._list.clear()

    def __len__(self):
        """ Количество элементов в очереди. """
        return self._len#
