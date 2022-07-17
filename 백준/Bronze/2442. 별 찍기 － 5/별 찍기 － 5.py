# 파이썬 기본
# 2442번 별 찍기 - 5

N = int(input())

for i in range(0, N):
    for j in range(N - 1, i, -1):
        print(" ", end = "")
    for j in range(0, 2 * i + 1):
        print("*", end = "")
    print()