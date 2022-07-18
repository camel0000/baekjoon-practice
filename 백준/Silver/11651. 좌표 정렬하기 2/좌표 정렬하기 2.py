# 정렬
# 11651번 좌표 정렬하기 2

N = int(input())
coord_ = []

for i in range(N):
    x, y = map(int, input().split())
    coord_.append([x, y])
    
coord_.sort(key = lambda x : (x[1], x[0]))

for i in range(N):
    print(coord_[i][0], coord_[i][1])