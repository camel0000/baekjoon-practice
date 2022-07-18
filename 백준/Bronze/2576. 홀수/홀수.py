# 파이썬 기본
# 2576번 홀수

list_ = []
list2_ = []
sum_ = 0

for i in range(7):
    list_.append(int(input()))
    
    if list_[i] % 2 == 1:
        sum_ += list_[i]
        list2_.append(list_[i])

if list2_:
    min_ = list2_[0]

    for i in range(len(list2_)):
        if min_ > list2_[i]:
            min_ = list2_[i]

    print(sum_)
    print(min_)
else:
    print(-1)