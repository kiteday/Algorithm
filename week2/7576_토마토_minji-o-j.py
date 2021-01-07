import sys
from collections import deque # 파이썬 queue 모듈 사용시 O(n)으로  collections.dequeue (O(1))에 비하여 많이 느리다.
box_size=sys.stdin.readline #속도 줄이기 위함
m,n=map(int, box_size().split()) #가로, 세로
checkfirst=-1 # 초기에 익어야 할 것 있나 확인용, 초기 -1, 익어야 할 것 있으면(0 존재) 1
top_ripe=deque() ## deque로 선언해야함!!

## 토마토 입력하기
tomato=[]
for i in range(n): #세로
    t_m=map(int, box_size().split()) #가로 토마토, 아까 받은거에서 잘라서 입력받음
    t_m=list(t_m) #형변환
    tomato.append(t_m)

    ## 익은 것의 위치를 찾는다(상위노드 찾기)
    for j in range(m): #가로
        if t_m[j]==1:
            top_ripe.append([i,j]) #행번호, 열번호
            
        elif t_m[j]==0: #아직 안익음, 방문 해야함
            checkfirst=0


#print(tomato) # 배열 입력 확인용
#print(state) #state 확인
'''
#큐 확인용
print(top_ripe)
print(top_ripe.popleft())
print(top_ripe)
'''

### BFS 함수
def BFS():
    '''
        #행(y), 열(x)로 구성
        dl=[di,dj-1] #왼쪽
        dr=[di,dj+1] #오른쪽
        df=[di+1,df] #앞
        db=[di-1,df] #뒤
    '''
    #위에거 자동화하기
    dy=[0,0,1,-1]
    dx=[-1,1,0,0]
    day=-1 #큐 안에 요소가 존재할 경우 마지막에 빠져나가는 것까지 한단계 더 거친다.
    
    while(top_ripe): #큐가 존재하면
        day+=1 #큐에 있는 것은 같은 선상이므로 하루 추가함
        r=len(top_ripe)
        for rr in range(r):
            di,dj=top_ripe.popleft() #행, 열

            for fway in range(4): # 좌우앞뒤
                y=di+dx[fway]
                x=dj+dy[fway]

                if(0<=x and x<m)and(0<=y and y<n)and(tomato[y][x]==0): #범위이내&안익은상태
                    tomato[y][x]=1 # 익히기 
                    top_ripe.append([y,x])

    for t in range(n): #행만큼
        if 0 in tomato[t]: #익지 않은 토마토가 있으면?
            return -1

    return day



        


### 익은 것부터 시작하여 BFS 수행
if checkfirst==-1: #저장될 때부터 모든 토마토가 익어있는 상태이면
    print(0)

else: #BFS 수행해야함
    print(BFS())
