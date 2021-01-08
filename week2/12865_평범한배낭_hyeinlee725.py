# N, K를 리스트로 반환
# N(1 ≤ N ≤ 100) : 물품의 수, K(1 ≤ K ≤ 100,000) : 무게
N, K = list(map(int, input().split()))

# 배열 계산을 위해 배열 크기는 (K + 1) * (N + 1)
# 배열을 0으로 초기화
bag = [[0 for col in range (K + 1)] for row in range(N + 1)]
# W(1 ≤ W ≤ 100,000), V(0 ≤ V ≤ 1,000)
W = [] # 물건 무게 배열
V = [] # 물건 가치 배열
W.append(0) # 배열 초기화
V.append(0) 

# W와 V는 N개의 줄에 거쳐서 주어지므로 for문을 통해 반환
for i in range(1, N+1):
    w, v = list(map(int, input().split()))
    W.append(w)
    V.append(v)
    for j in range(1, K+1):
        if j < W[i]: # 만약 이번에 넣을 무게(W)가 최대로 담을 수 있는 무게(j)보다 클 경우에는
            bag[i][j] = bag[i - 1][j] # 이전 가방의 값을 그대로 가져온다
        else: # j >= W - 만약 반대의 경우에는(이번에 넣을 무게(W)가 더 작은 경우)
            # 이전 물건까지 계산한 가방 무게 값과
            # 현재 넣을 물건의 가치(V) + 최대 무게(j) - 현재 물건의 무게(W[i])의 이전 값을 비교해서
            # 더 큰 값을 반환(만들 수 있는 최대의 가치를 만들기 위해)
            bag[i][j] = max(bag[i - 1][j], V[i] + bag[i - 1][j - W[i]])

print(bag[N][K]) # 가치의 최댓값을 출력
