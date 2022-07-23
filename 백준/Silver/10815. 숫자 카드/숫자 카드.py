# 이진 탐색(Binary Search)
# 10816번 숫자 카드 2

import sys
input = sys.stdin.readline

n = int(input())
N = list(map(int, input().split()))
N.sort()
m = int(input())
M = list(map(int, input().split()))

def binarySearch(target, data, start, end):
    if start > end:
        return 0
    
    mid = (start + end) // 2
    
    if data[mid] == target:
        return 1
    elif data[mid] < target:
        return binarySearch(target, data, mid + 1, end)
    else:
        return binarySearch(target, data, start, mid - 1)
        
for i in M:
    x = binarySearch(i, N, 0, len(N) - 1)
    print(x, end = " ")