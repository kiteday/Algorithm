# 파이썬 모듈 사용 - Queue 이용
from collections import deque

def bfs(x, y): # 주변에 있는 배추로 이동하므로 BFS 방식 이용
    # 배추가 있는지 확인하기 위한 queue 선언
    # deque 선언
    queue = deque()
    # queue에 배추밭에 있는 배추 위치 넣기
    queue.append((x, y))
    # queue에 값이 존재할 때(배추 존재)
    while (queue):
        x, y = queue.popleft() # Queue 처음에서 값을 pop(행, 열)
        
        for i in range(4): # 상하좌우(4번) 검사
            a = x + dx[i]
            b = y + dy[i]

            # 해당 범위 내에서 - 인접한 곳에 배추가 있는 경우
            if 0 <= a < N and 0 <= b < M:
                # field에 있는 값이 1이면(배추가 있으면)
                if field[a][b] == 1:
                    # 해당 field에 있는 값 -1로 바꾸기
                    # (해당 field에는 배추가 없는 것으로 바꾸기)
                    field[a][b] = -1
                    queue.append([a, b])

# 테스트 케이스 개수 입력
T = int(input())

# 인접한 다른 배추로 이동할 방향
dx = [-1, 1, 0, 0] # 좌우
dy = [0, 0, 1, -1] # 상하

# 각각의 테스트 케이스에 대해
for i in range(T):
    # 첫째줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50), 세로길이 N(1 ≤ N ≤ 50)
    # 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)
    M, N, K = map(int, input().split())
    # 배추밭 배열 선언
    field = [[0 for _ in range(M)] for _ in range(N)]
    # 배추흰지렁이 변수 선언 및 초기화
    white_earthworm = 0

    for j in range(K): # 배추 밭에 있는 배추 위치 반환
        # K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)
        X, Y = map(int, input().split())
        # 배추 위치 입력(배추밭 생성)
        field[Y][X] = 1

    # 배추 밭 확인
    for k in range(N):
        for l in range(M):
            # 만약 배추 밭에 배추가 존재하면
            if field[k][l] == 1:
                # bfs 실행
                bfs(k, l)
                # 배추흰지렁이 마리 수 추가(배추가 심어진 영역 수 추가)
                white_earthworm += 1

    # 각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수 출력
    print(white_earthworm)

