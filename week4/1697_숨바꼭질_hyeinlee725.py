# 파이썬 모듈 사용 - Queue 이용
from collections import deque

# 첫 번째 줄에 수빈이가 있는 위치 N, 동생이 있는 위치 K
# N과 K는 정수
N, K = map(int, input().split())
MAX = 100001
# 방문했는지 여부를 판단하기 위해 이동시간 저장(중복해서 방문하는 것을 막기 위해) 
time = [0 for _ in range(MAX)]

def bfs(N, K): # 주변에 동생이 있는지 확인하기 위해 이동하므로 BFS 방식 이용
    # 동생이 있는지 확인하기 위한 queue 선언
    # deque 선언
    queue = deque()
    # queue에 수빈이가 있는 출발 위치 넣기
    queue.append(N)
    
    while (queue): # queue가 존재하면
        # queue의 맨 앞 원소(현재 수빈이 위치) pop
        loc = queue.popleft()

        # 만약 동생을 찾으면
        if loc == K:
            # 위치 반환
            return time[loc]
        
        else: # 동생을 못 찾으면
            # 1초 후에 수빈이가 이동하게 될 위치 내에서
            # X-1 또는 X+1로 이동, 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동
            for i in (loc - 1, loc + 1, loc * 2):
                # 만약 수빈이 위치가 해당 범위 내에서
                # 그곳에 가본 적이 없는 경우
                if 0 <= i < MAX and not time[i]:
                    # 현재 위치에서 이동했으므로 1초 추가
                    time[i] = time[loc] + 1
                    # 이동한 위치 queue에 넣기
                    queue.append(i)

# 수빈이가 동생을 찾는 가장 빠른 시간 출력
print(bfs(N, K))
