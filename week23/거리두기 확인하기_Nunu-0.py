# [프로그래머스] 거리두기 확인하기
# 거리두기 검사
def Distancing(place, y, x, distance):
    loc = [0, 1, -1, 0]
    cnt = 0 
    
    for i in range(4):
        nx = x + loc[i % 4]
        ny = y + loc[(i + 2) % 4]
        
        if ny >= len(place) or ny < 0 or nx >= len(place[y]) or nx < 0:
            continue
        
        # 거리두기가 이루어지지 않았다면
        if place[ny][nx] == 'P':
            cnt += 1
            # 거리가 2일때는 자신도 찾기 때문에 cnt가 2일 때 
            if distance == 2 and cnt == 2: 
                 return 0
            if distance == 1 :
                return 0
        
        # 거리가 1일때 벽이 없다면 거리 2검사
        if place[ny][nx] == 'O' and distance == 1: 
            if Distancing(place, ny, nx, distance + 1) == 0:
                return 0
    return 1      

# 사람 찾기
def findPeople(place):
    for y in range(len(place)):
        for x in range(len(place[y])):
            # 사람을 찾았다면 거리두기 검사
            if place[y][x] == 'P':
                if Distancing(place, y, x, 1) == 0:
                    return 0
    return 1
            
def solution(places):
    answer = []
    
    for place in places:
        answer.append(findPeople(place))
        
    return answer