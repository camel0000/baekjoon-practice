# 파이썬 기본
# 10872번 팩토리얼

N = int(input())

result_ = 1

for i in range(1, N + 1):
    result_ *= i

print(result_)