# O(N^2) 시간복잡도를 가지는 다익스트라 알고리즘
import sys
input = sys.stdin.readline
v, e = map(int, input().split())
start = int(input())
INF = int(1e9)

visited = [False] * (v+1)  # 방문 여부
graph = [[] for _ in range(v+1)]  # 노드 연결 정보
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
distance = [INF] * (v+1)

def get_minimum():
    min_value = INF
    for i in range(2, v+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for i in graph[start]:
        distance[i[0]] = i[1]
    for _ in range(v-1):
        now = get_minimum()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, v+1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])