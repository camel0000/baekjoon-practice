# DP (Dynamic Programming)
# 9095번 1, 2, 3 더하기

T = int(input())

def calc_(n):
    if n == 1: return 1
    elif n == 2: return 2
    elif n == 3: return 4
    else: return calc_(n - 1) + calc_(n - 2) + calc_(n - 3)

for _ in range(T):
    n = int(input())
    print(calc_(n))