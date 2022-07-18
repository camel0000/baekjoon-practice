# 파이썬 기본
# 10809번 알파벳 찾기

S = input()

X = 'a'
cnt = 0

for i in range(26):
    for j in range(len(S)):
        if X == S[j]:
            cnt += 1
            index_ = j
            break
    
    if cnt != 0:
        print(index_, end = " ")
    else:
        print(-1, end = " ")

    cnt = 0
    X = ord(X) + 1
    X = chr(X)