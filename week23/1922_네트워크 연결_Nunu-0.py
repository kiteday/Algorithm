# [1922] 네트워크 연결
import heapq

# 연결 선 queue에 추가
def append(n):
    for i in line[n]:
        heapq.heappush(queue, i)

# a컴퓨터와 b컴퓨터 연결
def link(a, rst, cnt):
    while queue:
        c, b = heapq.heappop(queue) # 비용, b컴퓨터
        if not visit[b]:
            cnt += 1 
            rst += c
            visit[b] = True
            append(b)
        
        if cnt == N:
            return rst

N = int(input())
M = int(input())
line = [[] for _ in range(N + 1)] # 연결 할 수 있는 모든 선
queue = []
visit = [False] * (N + 1) # 컴퓨터를 연결했는지 확인

for _ in range(M):
    a, b, c = map(int, input().split())
    # 연결할 수 있는 선들 추가
    line[a].append([c, b])
    line[b].append([c, a])

# 부모 노드 설정(1)
visit[1] = True
append(1)

result = link(1, 0, 1)

print(result)
