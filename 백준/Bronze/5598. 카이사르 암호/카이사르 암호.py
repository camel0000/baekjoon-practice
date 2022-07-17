# 파이썬 기본
# 카이사르 암호

str_ = list(input())

for i in range(len(str_)):
    X = ord(str_[i]) - 3
    if X < ord('A'):
        X += ord('Z') - ord('A') + 1
    str_[i] = chr(X)
    
print("".join(str_))