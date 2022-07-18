# 파이썬 기본
# 1546번 평균

N = int(input())

list_ = list(map(int, input().split()))
M = max(list_)

for i in range(N):
    list_[i] = list_[i] / M * 100

avg_ = sum(list_) / len(list_)
print(avg_)