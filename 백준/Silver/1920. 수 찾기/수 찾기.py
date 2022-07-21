# 이진 탐색(Binary Search)
# # 1920번 수 찾기

N = int(input())
A = set(map(int, input().split()))
M = int(input())
X = list(map(int, input().split()))

for i in X:
    if i in A:
        print(1)
    else:
        print(0)