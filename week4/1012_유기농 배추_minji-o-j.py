import sys
sys.setrecursionlimit(10000) #재귀 한도 증가 
t=int(input()) #t: 테스트 케이스의 개수
#-----------------------------------
def BFS(cabbage,count,m,n,popflag,dx,dy): #cabbage: 배추 배열, m:가로, n:세로
    x_=[-1,1,0,0]
    y_=[0,0,-1,1]
    while(cabbage): #존재할 때
        
        if popflag==0:#랜덤으로 뽑아서 검사하기, 재귀함수로 실행되지 않은 경우 랜덤으로 뽑는다.
            count+=1
            dx,dy=cabbage.pop()
        else:
            cabbage.discard((dx,dy))
            
        for fway in range(4):#좌우앞뒤 검사
            x=dx+x_[fway]
            y=dy+y_[fway]

            if (0<=x and x<m)and(0<=y and y<n)and (x,y)in cabbage: #범위 이내
                BFS(cabbage,count,m,n,1,x,y)
            else:
                continue
            
        if popflag==1: #popflag(재귀함수)로 실행된 거면 종료
            break
            
    return count
        
#-----------------------------------
for i in range(t): #테스트 케이스의 개수 만큼 반복
    #print('---')
    cabbage=set([]) #배추배열 set
    input_=sys.stdin.readline
    m,n,k=map(int,input_().split()) #m: 배추밭의 가로 길이, n: 세로 길이, k: 배추가 심어진 위치의 개수

    for j in range(k): #k만큼 입력받음
        lst=tuple(map(int,input_().split())) #set에는 배열을 넣을 수 없으므로 튜플로 넣는다.
        cabbage.add((lst)) #큐에 추가
    
    print(BFS(cabbage,0,m,n,0,0,0))
