from collections import deque

'''
'BFS'로 탐색
토마토 문제 활용
양배추 배열에 값이 1인 것의 이웃(상하좌우) 탐색
탐색이 끝난 구역은 값을 1->0으로 변경해서 다시 방문하지 않도록함

(x,y)로 받은 좌표를 행렬로 하려니 너무헷갈림 ㅠ
'''

T=int(input())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
result = []

def BFS(y, x):
    mat = deque() #데크 선언
    mat.append([y,x]) #현재 양배추 위치 저장
    while len(mat)!=0:
        a, b = mat.popleft()
        for i in range(4): #현재 양배추의 상하좌우 탐색
            new_x = a + dx[i]
            new_y = b + dy[i]
            
            #이웃에 양배추가 있으면 데크에 위치 추가하고, 값은 0으로 변경
            if (0<=new_x<N) and (0<=new_y<M) and cabbage[new_x][new_y]==1:
                mat.append([new_x, new_y])
                cabbage[new_x][new_y]=0

for _ in range(T):
    M, N, K = map(int, input().split())
    cabbage=[[0]*M for i in range(N)]
    area = 0 #구역 몇 개인지 세는 변수

    for _ in range(K):
        x, y = list(map(int, input().split()))
        cabbage[y][x] = 1 #양배추가 있는 부분 표시
        
    for i in range(N):
        for j in range(M):
            if cabbage[i][j] == 1: #양배추가 있으면
                area += 1 #구역 하나 count
                BFS(i,j) #해당 좌표 이웃 탐색
                cabbage[i][j]=0 #이미 검사한 곳이니까 값을 0으로 변경시킴
    
    result.append(area) #각 테스트케이스별로 나오는 area를 result에 저장
    
for res in result:
    print(res)
