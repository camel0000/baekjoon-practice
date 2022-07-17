N = int(input())

for i in range(0, N):
    for j in range(i + 1, N):
        print(" ", end = "")
    for j in range(0, i + 1):
        print("*", end = "")
    print()