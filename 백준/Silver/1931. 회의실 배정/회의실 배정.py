import sys
input = sys.stdin.readline

N = int(input())
table = []

for i in range(N):
    s, e = map(int, input().split())
    table.append([s, e])
    
table.sort(key = lambda x:(x[1], x[0]))

count = 1
end = table[0][1]

for i in range(1, N):
    if table[i][0] >= end:
        count += 1
        end = table[i][1]
print(count)