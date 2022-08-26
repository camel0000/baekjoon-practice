import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N)]

for a in range(N):
    graph[a] = list(map(int, input().split()))

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
            # i에서 j로 직접 경로 있는 지 or i에서 다른 정점을 거쳐 j로 가는 경로 있는 지
                graph[i][j] = 1

for i in range(N):
    for j in range(N):
        print(graph[i][j], end = " ")
    print()