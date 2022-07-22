# 이진 탐색(Binary Search)
# 10816번 숫자 카드 2

n = int(input())
N = sorted(map(int, input().split()))
m = int(input())
M = map(int, input().split())

def binarySearch(target, data, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2
    
    if data[mid] == target:
        return data[start:end+1].count(target)
    elif data[mid] > target:
        return binarySearch(target, data, start, mid - 1)
    else:
        return binarySearch(target, data, mid + 1, end)

d = {}

for i in N:
    start = 0
    end = len(N) - 1
    
    if i not in d:
        d[i] = binarySearch(i, N, start, end)

for x in M:
    print(''.join(str(d[x]) if x in d else '0'), end = ' ')