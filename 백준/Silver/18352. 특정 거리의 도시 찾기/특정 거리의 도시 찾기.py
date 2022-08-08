# 다익스트라(Dijkstra) 알고리즘
# 18352번 특정 거리의 도시 찾기

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 10억 설정

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append((B, 1))

def dijkstra(start):
    q = []
    
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(X)

cnt = 0
for i in range(1, N + 1):
    if distance[i] == K:
        cnt += 1
        print(i)
if cnt == 0:
    print(-1)