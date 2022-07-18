# 정렬
# 1181번 단어 정렬

N = int(input())
list_ = []

for i in range(N):
    list_.append(input())
    
list_ = list(set(list_))
list_.sort()
list_.sort(key=len)

for i in list_:
    print(i)