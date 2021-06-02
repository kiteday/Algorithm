import sys
# [17265]나의 인생에는 수학과 함께
N = int(input())
board = [list(input().split()) for _ in range(N)]
loc = [0, 1]
maxi, mini = -1000000, 1000000

def dfs(x, y, sum, operator):
    global maxi, mini, board, N, loc

    for i in range(0, 2):  # 두자리 이동
        # 오른쪽 아니면 아래로 이동
        nx = x + loc[i]
        ny = y + loc[(i + 1) % 2]

        # 지도의 범위를 벗어나면
        if nx < N and ny < N:

            # 숫자가 아닌 연산자 부호라면 dfs
            if board[nx][ny] == '+':
                dfs(nx, ny, sum, '+')
            elif board[nx][ny] == '-':
                dfs(nx, ny, sum, '-')
            elif board[nx][ny] == '*':
                dfs(nx, ny, sum, '*')
            else:
                # 연산하기
                rst = 0
                if operator == '+':
                    rst = sum + int(board[nx][ny])
                elif operator == '-':
                    rst = sum - int(board[nx][ny])
                elif operator == '*':
                    rst = sum * int(board[nx][ny])
                dfs(nx, ny, rst, operator)

            # 마지막에 도착하면
            if nx == N - 1 and ny == N - 1:
                maxi = max(maxi, rst)
                mini = min(mini, rst)
                return

dfs(0, 0, int(board[0][0]), ' ')
print(maxi, mini)
