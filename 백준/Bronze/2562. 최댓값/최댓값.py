# 파이썬 기본
# 2562번 최댓값

list_ = []

for i in range(9):
    list_.append(int(input()))

max_ = list_[0]
index_ = 0

for i in range(9):
    if max_ < list_[i]:
        max_ = list_[i]
        index_ = i

print(max_)
print(index_ + 1)