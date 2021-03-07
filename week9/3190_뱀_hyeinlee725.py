import sys
from collections import deque

# 뱀 이동 방향 - 우 하 좌 상
dx=[1, 0, -1, 0]
dy=[0, 1, 0, -1]

# 이동 + 방향 변환
def move():
    # 초기 방향 : 오른쪽으로 이동
    direction = 0
    # 게임 진행 시간
    time = 0
    # 초기 뱀 위치(x, y) - 맨 위, 맨 좌측(0, 0)에서 시작
    x = 0
    y = 0
    visited = deque()
    # 방문한 위치 저장
    visited.append([y, x])
    # 뱀이 지나간 곳(2를 저장)
    board[y][x] = 2
    
    while True:
        time += 1
        # 뱀이 몸의 길이를 늘림
        x += dx[direction]
        y += dy[direction]

        # 보드 위에 있을 때, 지나가지 않은 경우 #
        if (0 <= y < N and 0 <= x < N and board[y][x] != 2):
            # 사과가 있는 경우 꼬리 그대로 유지 #
            if (board[y][x] == 1):
                board[y][x] = 2
                visited.append([y, x])
            
            # 사과가 없는 경우 꼬리 줄이기 #
            elif (board[y][x] == 0):
                board[y][x] = 2
                visited.append([y, x])
                # 꼬리 줄이기
                ty, tx = visited.popleft()
                board[ty][tx] = 0

            # 방향 전환을 해야하는 경우 #
            if (time in times):
                # 오른쪽으로 90도 방향 회전(D) : +1
                if (times[time] == "D"):
                    direction = (direction + 1) % 4                
                # 왼쪽로 90도 방향 회전(L) : -1
                else: # C == "L"
                    direction = (direction - 1) % 4
                    
        # 뱀이 자기자신의 몸 또는 벽과 부딪힌 경우
        else:
            # 게임 종료, 시간 반환
            return time

# Input
# 보드 크기(2 ≤ N ≤ 100)
N = int(input())
# 사과 개수(0 ≤ K ≤ 100)
K = int(input())
# N x N 정사각 보드 - 0으로 초기화
board = [[0 for _ in range(N)] for _ in range(N)]

# K개의 줄 - 사과의 위치
for _ in range(K):
    a, b = map(int, input().split())
    # 사과 위치 저장(1을 저장)
    board[a - 1][b - 1] = 1

# 뱀의 방향 변환 횟수(1 ≤ L ≤ 100)
L = int(input())
# 방향이 바뀌어야하는 시간 저장
times = {}

# L개의 줄 - 뱀의 방향 변환 정보
for i in range(L):
    # 정수 X, 문자 C
    X, C = input().split()
    times[int(X)] = C

# 게임이 몇 초에 끝나는지 print
print(move())
