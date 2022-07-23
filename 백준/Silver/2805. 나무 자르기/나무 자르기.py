# 이진 탐색(Binary Search)
# 2805번 나무 자르기

N, M = map(int, input().split())
H = list(map(int, input().split()))

start = 1
end = max(H)

while start <= end:
    mid = (start + end) // 2
    len_ = 0
    
    for i in H:
        if i >= mid:
            len_ += (i - mid)
    
    if len_ >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)