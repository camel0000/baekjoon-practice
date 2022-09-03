from collections import Counter

import sys
input = sys.stdin.readline

N = int(input())
List = []

for _ in range(N):
    List.append(int(input()))
List.sort()

cnt = Counter(List).most_common(2)

# 산술평균
print(round(sum(List) / N))
# 중앙값
print(List[N // 2])
# 최빈값 구하기
if N > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
# 범위
print(max(List) - min(List))