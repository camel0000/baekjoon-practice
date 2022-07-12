N = int(input())
P = list(map(int, input().split()))
P.sort()

time = 0

for i in range(0, N):           # operating all array
    for j in range(0, i+1):
        time += P[j]

print(time)