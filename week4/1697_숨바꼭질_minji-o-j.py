from collections import deque
n,k=map(int,input().split()) #n: 수빈이가 있는 위치, k: 동생이 있는 위치
check=[0 for i in range(100001)] #이동 횟수 저장(중복 피하기 위함)


'''
모든 경우의 수를 따짐 -> 한 단계 더 갈 때(+1,-1,*2)가 모두 비용이 같으므로 BFS이용
'''
def BFS(n,k): 
    go=deque()
    go.append(n) # 시작, 수빈이가 있는 시작 위치를 큐에 삽입
    
    while(go): #go 큐가 존재하면
        x=go.popleft() #큐의 맨 앞 원소, 현재 수빈이 위치
        move=[x-1,x+1,2*x] # x(수빈이) 이동 배열
        
        if x==k: #동생 찾음
            return check[x]
            
        else: # 동생 못찾음
            for i in move: # i: 수빈이가 이동할 위치(다음번 수빈이의 위치)
                if(0<=i<=100000) and check[i]==0: # 이동하려고 하는 수빈이 위치가 범위 만족할 경우, 그곳을 처음 가봤을 경우에만 실행
                    check[i]=check[x]+1 # 현재 상태(x)에서 이동했으므로 비용 1(1초)추가
                    go.append(i) # 이동한 위치 큐에 넣음 

print(BFS(n,k))
