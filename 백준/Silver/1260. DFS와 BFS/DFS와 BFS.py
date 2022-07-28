# DFS & BFS (깊이우선탐색 & 너비우선탐색)
# 1260번 DFS와 BFS

from collections import deque

def dfs(v):
    visited[v] = True
    print(v, end = ' ')
    
    for i in range(1, N + 1):
        if visited[i] == False and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited[v] = True
    
    while queue:
        p = queue.popleft()
        print(p, end = ' ')
        
        for i in range(1, N + 1):
            if visited[i] == False and graph[p][i] == 1:
                queue.append(i)
                visited[i] = True

N, M, V = map(int, input().split())

graph = [[0] * (N + 1) for i in range(N + 1)]

for i in range(M):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

visited = [False] * (N + 1)
dfs(V)
print()

visited = [False] * (N + 1)
bfs(V)