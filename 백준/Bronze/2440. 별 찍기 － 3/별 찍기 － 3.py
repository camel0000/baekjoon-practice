# 파이썬 기본
# 2440번 별 찍기 - 3

N = int(input())

for i in range(N, 0, -1):
    for j in range(0, i):
        print("*", end = "")
    print()