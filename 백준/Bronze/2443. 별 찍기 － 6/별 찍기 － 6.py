# 파이썬 기본
# 2443번 별 찍기 - 6

N = int(input())

for i in range(N, 0, -1):
    for j in range(i, N):
        print(" ", end = "")
    for j in range(0, 2 * i - 1):
        print("*", end = "")
    print()