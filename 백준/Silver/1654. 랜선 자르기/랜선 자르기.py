# 이진 탐색(Binary Search)
# 1654번 랜선 자르기
    
K, N = map(int, input().split())
list_ = []

for i in range(K):
    list_.append(int(input()))

start = 1
end = max(list_)

while start <= end:
    mid = (start + end) // 2
    
    count = 0
    
    for i in list_:
        count += (i // mid)
        
    if count >= N:
        start = mid + 1
    else:
        end = mid - 1
    
print(end)