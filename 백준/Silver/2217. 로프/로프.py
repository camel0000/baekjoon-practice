# 2217번 로프 (Greedy)

N = int(input())
max_weights = [int(input()) for _ in range(N)]

max_weights.sort(reverse=True)    # 리스트 내림차순 정렬

results = []

for i in range(N):
    results.append(max_weights[i] * (i + 1))
    
print(max(results))