import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))

X_ = sorted(list(set(X)))

dic = {X_[i] : i for i in range(len(X_))}

for i in X:
    print(dic[i], end = " ")