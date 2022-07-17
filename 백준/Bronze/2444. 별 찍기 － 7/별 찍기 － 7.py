# 파이썬 기본
# 2444번 별 찍기 - 7

N = int(input())

for i in range(0, N):
    for j in range(i, N - 1):
        print(" ", end = "")
    for j in range(0, 2 * i + 1):
        print("*", end = "")
    print()

for i in range(N - 1, 0, -1):
    for j in range(i, N):
        print(" ", end = "")
    for j in range(0, 2 * i - 1):
        print("*", end = "")
    print()