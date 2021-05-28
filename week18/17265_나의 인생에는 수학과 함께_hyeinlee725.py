import sys

# 지도의 크기 N(3 ≤ N ≤ 5, N은 홀수)
N = int(sys.stdin.readline())
# N 줄에는 N개의 숫자 또는 연산자
route_map = [list(input().split()) for _ in range(N)]
# 연산 결과의 최댓값, 최솟값
max_res = -1e9
min_res = 1e9
# 방향(오른쪽, 아래만 탐색)
direc = [[1, 0], [0, 1]]

# 연산 결과 계산하는 함수
def calc(x, y, res, oper):
    global max_res, min_res
    # 연산자가 +, -, *인 경우 각각 계산
    if (oper == '+'):
        res += int(route_map[x][y])
    elif (oper == '-'):
        res -= int(route_map[x][y])
    elif (oper == '*'):
        res *= int(route_map[x][y])

    # 정해진 방향으로 이동
    for dx, dy in direc:
        dx = x + dx
        dy = y + dy
        # 지도 내에 존재하면 각 연산 실행
        if (0 <= dx < N and 0 <= dy < N):
            if (route_map[x][y] == '+'):
                calc(dx, dy, res, '+')
            elif (route_map[x][y] == '-'):
                calc(dx, dy, res, '-')
            elif (route_map[x][y] == '*'):
                calc(dx, dy, res, '*')
            else: # 숫자인 경우
                calc(dx, dy, res, -1)
        
        # 마지막 칸인 경우, 최댓값과 최솟값을 찾아서 return
        if (x == N - 1 and y == N - 1):
            max_res = max(max_res, res)
            min_res = min(min_res, res)
            return

calc(0, 0, 0, '+')
print(max_res, min_res)
