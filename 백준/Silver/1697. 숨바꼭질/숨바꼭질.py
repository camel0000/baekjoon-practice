# DFS & BFS (깊이우선탐색 & 너비우선탐색)
# 1697번 숨바꼭질

from collections import deque

def bfs():
    Q = deque()
    Q.append(N)
    
    while Q:
        p = Q.popleft()
        
        if p == K:
            return visited[p]
        
        for i in (p - 1, p + 1, p * 2):
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[p] + 1
                Q.append(i)

N, K = map(int, input().split())
visited = [0] * 100001      # (최대 범위 100000) + 1 

print(bfs())