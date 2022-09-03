import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))

P.sort()

sum_ = 0
for i in range(N):
    for j in range(0, i + 1):
        sum_ += P[j]
print(sum_)