import heapq
from typing import List, Tuple


def dijkstra(graph: List[List[Tuple[int, int]]], start: int) -> List[int]:
    """
    1. 将(start,0)加入heap中
    2. 弹出heap，如果当前点i到start的distance大于distances[i]，直接跳过
    3. 遍历点i的所有邻近点j，如果小于distances[j]，加入队列中
    4. 重复上述步骤
    :param graph: 图，点->(点,距离)
    :param start: 起点
    :return: 顶点到每个点的最短路径
    """
    distances = [float('inf')] * len(graph)  # 维护到源点的最短距离
    heap = [(0, start)]  # 最小堆
    while heap:
        currDis, node = heapq.heappop(heap)  # 每次取出到源点距离最短的点
        # 如果最短的点都小于一直最短距离的点，说明已经被其他点维护过了，这个点不可能是到达其他点的最小距离的点了，直接跳过
        if currDis > distances[node]:
            continue
        # 遍历每一个当前点的邻接点，看看有没有比当前distances还小的点
        for nei, wei in graph[node]:
            dis = currDis + wei
            # 如果距离小于当前最短距离，则更新
            if dis < distances[nei]:
                distances[nei] = dis
                # 加入当前点和当前距离到最小堆中
                heapq.heappush(heap, (dis, nei))
    return distances


# 示例
graph = [
    [(1, 4), (2, 1)],  # 邻接列表表示，例如：顶点0连接到顶点1和2，边的权重分别是4和1
    [(3, 1)],
    [(1, 2), (3, 5)],
    [(4, 3)],
    []
]
start_vertex = 0
print(dijkstra(graph, start_vertex))  # 输出从顶点0到所有其他顶点的最短距离
