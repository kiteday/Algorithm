import sys
Paper = sys.stdin.readline #속도 조절용

# 시험지의 개수 N, 시험지를 나눌 그룹의 수 K
# (1 ≤ K ≤ N ≤ 105)
N, K = list(map(int, Paper().split()))

# 각 시험지마다 맞은 문제의 개수 x(0 ≤ x ≤ 20)
x = [] # 배열 생성
x.extend(list(map(int, Paper().split()))) # x를 배열에 저장
    
def calculate(n): # 점수 계산함수
    group = 1 # 그룹 개수
    score_sum = 0 # 점수를 더한 변수
    for i in range(N): # 시험지 개수마다
        score_sum += x[i] # x에 있는 변수만큼 더하고
        
        # 그룹 내 점수가 n 이상이 되면 그룹 자르기
        if (score_sum > n):
            group += 1 # 그룹 개수 증가
            score_sum = 0 # 점수 초기화
            
    return group <= K # 그룹 개수가 K개 보다 작거나 같을 때 반환

minimum = 0 # 최소 점수
maximum = max(x) * N + 1 # 최대 점수

while minimum + 1 < maximum: # 다음과 같을 동안
    mid = (minimum + maximum) // 2 # mid는 다음과 같다
    
    if (calculate(mid)): # 점수 계산 함수를 통한 계산
        # 그룹의 개수가 K보다 작은 경우
        maximum = mid # 최대 점수를 mid로 내리고
    else: # 반대의 경우
        minimum = mid # 최소 점수를 mid로 올린다

print(maximum) # 현수가 받을 수 있는 최대 점수 출력
