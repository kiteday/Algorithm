# [프로그래머스] 삼각 달팽이
def solution(n):
    answer = []
    list = [[0 for k in range(0,i+1)] for i in range(0,n)]
    x, y, cnt = -1, 0, 1
    
    for i in range(n):
        for j in range(i, n):
            # 달팽이 마냥 돌아간다
            if i % 3 == 0: # 아래로 이동 
                x += 1
            elif i % 3 == 1: # 오른쪽으로 이동
                y += 1
            elif i % 3 == 2: # 북서방향으로 이동
                x -= 1
                y -= 1
            
            list[x][y] = cnt;
            cnt += 1
                
    for i in range(n):
        for j in range(0, i+1):
            answer.append(list[i][j])
            
    return answer