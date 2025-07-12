from typing import Union
import networkx as nx
import heapq


def build_graph(stairway):
    graph = {}
    n = len(stairway)
    for i in range(-1, n):
        graph[i] = []
        if i + 1 < n:
            graph[i].append((i + 1, stairway[i + 1]))
        if i + 2 < n:
            graph[i].append((i + 2, stairway[i + 2]))
    return graph

def build_graph(stairway):
    G = nx.DiGraph()
    n = len(stairway)
    for i in range(-1, n):
        if i + 1 < n:
            G.add_edge(i, i + 1, weight=stairway[i + 1])
        if i + 2 < n:
            G.add_edge(i, i + 2, weight=stairway[i + 2])
    return G


def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    if not stairway:
        return 0
    n = len(stairway)
    graph = build_graph(stairway)

    distance = {i: float('inf') for i in range(-1, n)}
    distance[-1] = 0

    heap = []
    heapq.heappush(heap, (0, -1))

    while heap:
        current_dist, u = heapq.heappop(heap)
        if current_dist > distance[u]:
            continue
        for v, weight in graph.get(u, []):
            if distance[v] > distance[u] + weight:
                distance[v] = distance[u] + weight
                heapq.heappush(heap, (distance[v], v))

    return distance[n - 1]






if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)
    stairway_graph = build_graph(stairway)
    print(stairway_path(stairway_graph))  # 72
