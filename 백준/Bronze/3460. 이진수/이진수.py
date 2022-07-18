# 파이썬 기본
# 3460번 이진수

T = int(input())

N = []

for i in range(T):
    N.append(int(input()))
    N[i] = format(N[i], 'b')
    
    X = list(N[i])
    X.reverse()
    
    for j in range(len(X)):
        if X[j] == '1':
            print(j, end = " ")
    print()