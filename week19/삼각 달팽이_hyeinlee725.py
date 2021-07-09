def solution(n):
    answer = []
    # 밑변, 높이가 n인 삼각형 배열
    tri_map = [[0 for _ in range(n)] for _ in range(n)]
    # 좌표값(처음에 아래로 내려가므로 x는 -1)
    x, y = -1, 0
    cnt = 1
    # 달팽이가 반시계 방향으로 회전
    for i in range(n):
        for j in range(i, n):
            if(i % 3 == 0): # 나머지가 0이면 아래로 이동
                x += 1
            elif(i % 3 == 1): # 나머지가 1이면 오른쪽으로 이동
                y += 1
            else: # 나머지가 2이면 위로 이동
                x -= 1
                y -= 1
            tri_map[x][y] = cnt
            cnt += 1
    # 첫 행부터 마지막 행까지 순서대로 합치기(0 제외)
    for i in tri_map:
        for j in i:
            if(j != 0):
                answer.append(j)
    return answer
