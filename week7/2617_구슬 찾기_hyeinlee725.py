# 파이썬 모듈 사용 - Queue 이용
from collections import deque
import sys
marble = sys.stdin.readline # input

# 구슬의 개수를 나타내는 정수 N(1 ≤ N ≤ 99)
#  M ≤ N(N-1)/2)
N, M = map(int, input().split())

heavy_m = [[] for _ in range(N + 1)] # 무거운 구슬 저장 list
light_m = [[] for _ in range(N + 1)] # 가벼운 구슬 저장 list

marble_cnt = 0 # 중간이 될 수 없는 구슬의 수
mid = (N + 1) // 2 # 전체의 중간(무게 순서로 (N+1)/2번째)

for _ in range(M): # M 개의 줄마다 구슬 번호 주어짐
    # 앞 번호의 구슬이 뒤 번호의 구슬보다 무거움
    H, L = map(int, input().split())
    heavy_m[L].append(H) # 각각 list에 저장
    light_m[H].append(L)

# DFS로 시도했을 때는 시간 초과가 일어남
# 모든 정점을 방문 - 완전 탐색
def bfs(data_list, node):
    # check하는 배열 - 방문한 구슬인지 확인하는 목적
    # False로 기초
    check = [False for _ in range(N + 1)]
    # 방문한 node는 True로
    check[node] = True
    q = deque()
    q.append(node)
    cnt = 0

    while (len(q) != 0): # q에 값이 존재하면
        node = q.popleft()
        
        for n in data_list[node]: # 해당 list에 있는 값이
            if(check[n] == False): # False이면 - 방문 X
                check[n] = True # True로 바꾸고 - 방문 완료
                cnt += 1
                if (cnt >= mid):
                    return 1 # 1을 더해줄 목적
                q.append(n)
    return 0 # 위에 해당되지 않으면 0을 반환

for i in range(1, N + 1):    
    marble_cnt += bfs(heavy_m, i) # 무거운 구슬
    marble_cnt += bfs(light_m, i) # 가벼운 구슬

print(marble_cnt)
