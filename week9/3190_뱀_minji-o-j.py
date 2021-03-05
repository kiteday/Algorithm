from collections import deque
import sys
n=int(input()) # 보드의 크기
k=int(input()) # 사과의 개수
apple=set([]) #사과의 위치 저장 
for _ in range(k):
    a,b=map(int,input().split()) #x,y로 받았는데
    apple.add((b,a)) #행열로 입력이라서 바꿔줌 ㅠ
    
l=int(input()) # 뱀의 방향 변환 횟수
snake=deque() #뱀의 방향 변환 정보 저장
for _ in range(l):
    x,c=input().split() # x: 게임 시작시간으로부터 x초가 끝난 이후 c방향(L:왼, D:오)으로 회전
    snake.append([int(x),c])


## 뱀 이동
snake_x=[1,0,-1,0] #오른쪽, 아래, 왼쪽, 위
snake_y=[0,1,0,-1]
move=0 #초기: 오른쪽으로 이동

timer=0 #x초
head=[1,1]
tail=[1,1]
tail_list=deque()
tail_list.append([1,1]) #초기 head 저장



while(1):    
    timer+=1
    
    ## 뱀은 몸길이를 늘린다
    head[0]+=snake_x[move]
    head[1]+=snake_y[move]
    tail_list.append(head.copy())
    
    if 1<=head[0]<=n and 1<=head[1]<=n: #박스(?) 범위 내일때만
        ## 사과가 머리에 있으면 먹겠지?
        try:
            apple.remove(tuple(head)) #사과 먹기, 꼬리 움직이지 않음
            
        except KeyError: #머리 위치에 사과가 없음 -> 꼬리 위치한 칸 비움
            tail=tail_list.popleft()
            
        ## 자신 몸과 부딪히면 종료
        for i in list(tail_list)[:-1]:
            if head==i or head==tail:
                print(timer)
                sys.exit(0)
        
    else: ## 벽에 부딪히면 종료
        break


    
    ## 회전해야 하는 경우
    if snake:
        if timer==snake[0][0]:
            _,direct=snake.popleft() #D: 오른쪽으로 90도회전, L: 왼쪽으로 90도 회전

            if direct=='D':
                move=(move+1)%4
            else:
                move=(move-1)%4

print(timer)
