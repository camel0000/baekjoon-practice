# DFS & BFS (깊이우선탐색 & 너비우선탐색)
# 1012번 유기농배추

import sys
sys.setrecursionlimit(2550)

def dfs(a, b):
    if a < 0 or b < 0 or a >= N or b >= M:
        return False
    
    if matrix_[a][b] == 1:
        matrix_[a][b] = 0
        
        dfs(a - 1, b)   # 상
        dfs(a + 1, b)   # 하
        dfs(a, b - 1)   # 좌
        dfs(a, b + 1)   # 우
        
        return True
    
    return False

T = int(input())

for t in range(T):
    M, N, K = map(int, input().split())
    
    matrix_ = [[0 for _ in range(M)] for _ in range(N)]     # 행렬 0으로 초기화

    for i in range(K):
        y, x = map(int, input().split())
        matrix_[x][y] = 1

    count_ = 0
    for i in range(N):
        for j in range(M):
            if dfs(i, j) == True:
                count_ += 1
    print(count_)