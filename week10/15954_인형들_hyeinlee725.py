import sys

# 서로 다른 N개의 인형(1 <= N <= 500)
N, K = map(int, input().split())
# 인형을 선호하는 사람의 수(10의 6승 이하의 음이 아닌 정수)
prefer_num = list(map(int, input().split()))
# 표준 편차 배열
std_dev = []

# K개 이상의 연속된 위치(1 <= K <= N)
for i in range(K, N + 1):
    for j in range(N - i + 1):
        # N개의 수 a1, a2, …, aN
        N_list = prefer_num[j:(i + j)]
        # (산술) 평균
        m = sum(N_list) / i
        # 분산
        var = sum([(x - m) ** 2 for x in N_list]) / i
        # 표준 편차(분산의 제곱근으로 정의)
        std_dev.append(var ** 0.5)

# 선택된 인형들을 선호하는 사람의 수의 표준 편차 출력     
print(str(min(std_dev)))
