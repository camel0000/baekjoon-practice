# 정렬
# 11650번 좌표 정렬하기

N = int(input())

coord_ = []

for i in range(N):
    X, Y = map(int, input().split())
    coord_.append([X, Y])

coord_.sort()

for i in range(N):
    print(coord_[i][0], coord_[i][1])