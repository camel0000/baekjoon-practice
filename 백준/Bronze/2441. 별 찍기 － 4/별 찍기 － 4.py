# 파이썬 기본
# 2441번 별 찍기 - 4

N = int(input())

for i in range(N, 0, -1):
    for j in range(N, i, -1):
        print(" ", end = "")
    for j in range(0, i):
        print("*", end = "")
    print()