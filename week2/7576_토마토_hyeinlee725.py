# 파이썬 모듈 사용 - Queue 이용
from collections import deque

# M, N을 반환(M : 상자의 가로 칸의 수, N : 상자의 세로 칸의 수)
# 단, 2 ≤ M,N ≤ 1,000
M, N = map(int, input().split())

# 토마토 상자 배열(ripe_tomato은 익은 토마토 상자 배열)
# deque 선언
tomato_box, ripe_tomato = [], deque()

# 인접한 토마토가 익는 방향
dx = [-1, 1, 0, 0] # 좌우
dy = [0, 0, 1, -1] # 상하

for i in range(N):
    row = list(map(int, input().split())) # 입력된 토마토 값 가져옴
    for j in range(M):
        if row[j] == 1: # 토마토가 익었으면
            ripe_tomato.append([i, j]) # ripe 배열에 추가
    tomato_box.append(row) # 토마토 상자 배열에 값 추가

def bfs(M, N, tomato_box): # 토마토의 주변이 익는 것이므로 BFS 방식 이용
    
    day = -1 # 날짜는 -1에서 시작
    #(큐 안에 마지막 요소가 빠져나가는 것까지 하루 더 추가되므로 -1에서 시작)

    while (ripe_tomato): # 토마토가 익었으면(ripe_tomato 배열)
        day += 1 # 하루 추가
        
        for i in range(len(ripe_tomato)):
            x, y = ripe_tomato.popleft() # Queue 처음에서 값을 pop(행, 열)

            for j in range(4): # 상하좌우(4번)
                a = x + dx[j]
                b = y + dy[j]

                if 0 <= a < N and 0 <= b < M: # 해당 범위 내에서
                    if tomato_box[a][b] == 0: # 만약 토마토가 아직 안익은 경우
                        tomato_box[a][b] = tomato_box[x][y] + 1 # 토마토를 익히기
                        ripe_tomato.append([a, b]) # ripe 배열에 추가

    for k in tomato_box: # tomato_box 배열 만큼
        if 0 in k: # 토마토가 익지 않은 것이 존재하면
            return -1 # -1을 출력(토마토가 모두 익지 못하는 상황)
        
    return day # 날짜를 반환
  
print(bfs(M, N, tomato_box)) # 날짜 출력
# 토마토가 모두 익어있는 상태면 일단 ripe_tomato를 추가하기 위해
# 하루가 추가 되므로 day가 0이 된다.
