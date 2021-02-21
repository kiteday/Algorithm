# 브루트포스 알고리즘(DFS : Back Tracking, BFS : 브루트포스)
import sys
from collections import deque
input = sys.stdin.readline

# BFS - 그룹의 모든 원소가 서로 연결되었는지 확인하는 함수
def connection_check(group):
    queue = deque()
    visited = [False for _ in range(N + 1)]# 방문한 배열
    queue.append(group[0]) # 시작점 큐에 저장
    visited[group[0]] = True # 시작점 방문완료
    cnt = 1 # 연결된 도시 개수
    
    while queue:
        x = queue.popleft()
        for i in group:
            # 같은 지역구(인접)이고, 방문한 적이 없는 경우
            if (adj_list[x][i] == 1 and visited[i] == 0):
                # queue에 저장
                queue.append(i)
                # 방문완료
                visited[i] = True
                # 도시 + 1
                cnt += 1
    # 이어져 있으면 1, 아니면 0 반환
    # 연결된 도시 개수가 도시 집합의 크기와 같으면 모두 연결
    if (cnt == len(group)):
        return 1
    else:
        return 0

# 그룹 set - 2개의 그룹으로 묶음
def set_group(k):
    global res
    if k == N + 1:
        g1 = deque() # group1
        g2 = deque() # group2
        
        # 2개의 그룹으로 나눠서 저장 #
        for i in range(1, N + 1):
            if include[i]:
                g1.append(i)
            else:
                g2.append(i)
                
        # poplulation sum 계산 # 
        # 각 그룹의 인구수 총합 계산
        sum_g1 = 0
        sum_g2 = 0
        for i in g1:
            sum_g1 += population[i]
        for i in g2:
            sum_g2 += population[i]

        # 도시 길이가 0이 아니고
        if (len(g1) != N and len(g1) != 0 and len(g2) != N and len(g2) != 0):
            # 두 개의 그룹 모두 연결되어 있을 경우 인구수 차를 계산
            if (connection_check(g1) and connection_check(g2)):
                # 차이 계산, 최소값 찾기
                dis = abs(sum_g1 - sum_g2)
                if (res > dis):
                    res = dis
        return
    include[k] = 1
    set_group(k+1)
    include[k] = 0
    set_group(k+1)
    
N = int(input()) # 구역 개수 N(2 ≤ N ≤ 10)
# 1 ~ N 구역의 인구수(1 ≤ 구역의 인구 수 ≤ 100)
population = list(map(int,input().split())) 
population.insert(0, 0) # 맨 앞에 0 추가
# 결과값 - 인구 차이 최솟값(가장 큰 값에서 점점 줄여나감)
res = sys.maxsize 

# 구역별 인접 여부 저장 list
adj_list = [[0 for _ in range(N + 1)]for _ in range(N + 1)]
# 포함 여부 저장 list
include = [0 for _ in range(N + 1)] 

for a in range(1, N + 1): # 1 ~ N 구역에 연결된 도시 정보를 입력받아 인접행렬로 표시
    # 각 구역과 인접한 구역의 정보
    # (첫 번째 정수는 그 구역과 인접한 구역의 수이고, 이후 인접한 구역의 번호)
    adj_area = list(map(int,input().split()))
    # a 도시에 연결된 b 도시
    for b in adj_area[1:]: # 첫번째 정수는 연결 개수이므로 제외
        # 각각 인접함을 표시
        adj_list[a][b] = 1
# group 묶어서 연결 확인 및 인구수 차 계산
set_group(1)

# 인구차이 최솟값 출력, 나눌 수 없는 경우 -1 출력
if (res == sys.maxsize):
    print(-1)
else:
    print(res)
