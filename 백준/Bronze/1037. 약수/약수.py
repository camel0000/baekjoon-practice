# 파이썬 기본
# 1037번 약수

N = 1

divisor_N = int(input())
list_divisors_ = list(map(int, input().split()))

max_ = list_divisors_[0]
min_ = list_divisors_[0]

for i in range(divisor_N):
    if max_ < list_divisors_[i]:
        max_ = list_divisors_[i]
    if min_ > list_divisors_[i]:
        min_ = list_divisors_[i]

N = max_ * min_
print(N)