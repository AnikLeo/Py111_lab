

# 1.	Оценить асимптотическую сложность приведенного ниже алгоритма:
# a = len(arr) - 1
# out = list()
# while a > 0:
#     out.append(arr[a])
#     a = a // 1.7
# out.merge_sort()

a = len(arr) - 1  - O(1)

out = list() - O(1)

while a > 0:
    out.append(arr[a])
    a = a // 1.7 - O(log n) - O(log n * log(log n))

Итоговая сложность: O(log n) - O(log n * log(log n))

# 2.	Считалочка
# Дано N человек, считалка из K слогов. Считалка начинает считать с первого человека. Когда считалка досчитывает до k-го слога, человек, на котором она остановилась, вылетает. Игра происходит до тех пор, пока не останется последний человек. Для данных N и К дать номер последнего оставшегося человека.

def last_person_number(N, K):
    result = 0
    for i in range(1, N + 1):
        result = (result+ K) % i
    return result + 1

# 3.	Назовем связным такой граф, в котором есть путь от любой вершины к любой другой вершине.
# Дан граф, состоящий из 2+ связных подграфов, которые не связаны между собой.
# Задача: посчитать число компонент связности графа, т.е. количество таких подграфов.
# В графе на картинке – три подграфа, т.е. число компонент связности = 3.

def dfs(graph, vertex, visited):
    visited[vertex] = True
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def count_components(graph):
    visited = {i: False for i in graph}
    count = 0
    for i in graph:
        if not visited[i]:
            dfs(graph, i, visited)
            count += 1
    return count

graph = {
    0: [1],
    1: [0],
    2: [3],
    3: [2],
    4: [5],
    5: [4]
}

print(f"Количество подграфов: {count_components(graph)}")

# 6.	Аренда ракет
# Вы – компания, дающая в аренду ракеты. Каждый день к вам приходит список заявок на использование ракет в виде: (час_начала, час_конца), (час_начала, час_конца), ...
# Если аренда ракеты заканчивается в час X, то в этот же час ее уже можно взять в аренду снова (т.е. час_начала может начинаться с Х).
# Дано: список заявок на использование ракет
# Задача: вывести ответ, хватит ли вам одной ракеты, чтобы удовлетворить все заявки на этот день

def one_rocket_rent(requests):
    if not requests:
        return True

    requests.sort()

    for i in range(1, len(requests)):
        rent_start, rent_end = requests(i-1)
        current_start, current_end = requests[i]

        if current_start < rent_end:
            return False

    return True

# 7.	Сорт
    # Дано: массив из 10**6 целых чисел, каждое из которых лежит на отрезке [13, 25].
    # Задача: отсортировать массив наиболее эффективным способом

def count_sort(arr):
    min_val = 13
    max_val= 25
    count = [0] * (max_val - min_val + 1)

    for num in arr
        count[num - min_val] +=1

    index = 0
    for i in range(range_size):
        while count[i] > 0:
            arr[index] = i + min_val
            index += 1
            count[i] -= 1

    return arr




