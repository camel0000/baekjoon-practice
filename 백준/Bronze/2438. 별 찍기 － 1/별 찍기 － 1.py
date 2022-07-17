# 파이썬 기본
# 2438번 별 찍기 - 1

N = int(input())

for i in range(0, N):
    for j in range(0, i + 1):
        print("*", end = '')
    print()