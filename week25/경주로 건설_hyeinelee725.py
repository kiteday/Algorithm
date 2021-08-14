from collections import deque
def solution(board):
    # 좌, 하, 상, 우
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    queue.append([0, 0, -1, 0]) # x, y좌표, direction, 건설 비용
    N = len(board)
    # 경주로 부지
    track_Board = [[0] * N for _ in range(N)]
    while queue:
        # x, y좌표, 방향, 비용을 각각 pop
        x, y, direc, cost = queue.popleft()
        for d in range(4): # 상하좌우(4번)
            nx = x + dx[d]
            ny = y + dy[d]
            # 해당 범위 내에서
            if (0 <= nx < N and 0 <= ny < N and not board[ny][nx]):
                # 방향이 바뀌지 않으면(직선 도로)
                if (direc == -1):
                    # 100원 소요
                    newcost = cost + 100
                # 기존 방향과 진행 방향이 평행
                elif (direc == d):
                    # 100원 소요
                    newcost = cost + 100
                else: # 수직인 경우 600원 소요
                    newcost = cost + 600
                # 처음 방문하거나, 더 적은 비용이 드는 경
                if (track_Board[ny][nx] == 0 or track_Board[ny][nx] >= newcost):
                    # 값을 바꾸고, queue에 저장
                    track_Board[ny][nx] = newcost
                    queue.append((nx, ny, d, newcost))
    # 최소값 return
    return track_Board[-1][-1]
