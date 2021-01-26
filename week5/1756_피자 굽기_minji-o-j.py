import sys
d,n=map(int,input().split()) # d: 오븐의 깊이, n: 피자 반죽의 개수
oven=list(map(int,input().split())) # 오븐의 지름 - 최상단부터 주어짐
pizza_d=list(map(int,input().split()))  # 피자 반죽 지름 - 완성된 순서대로

#----------------------
'''
위에부터 넣어서 못넣는 곳 이전에에 피자 위치 시킴 --> 시간 초과
알고리즘 이분탐색 -> 정렬불가 -> 그릇 모양?으로 하면 정렬된 형태
1) 오븐을 그릇 모양으로 만든다
2) 피자를 넣는다
- 이분탐색할 때 숫자가 중복이 있어서 index로 접근해야할듯?
'''

#----------------------
## 그릇모양 만들기 함수
def bowl(oven,d):
    width=oven[0]

    for i in range(1,d):
        if  oven[i]<width:
            width=oven[i]
        else: #크거나 같음
            oven[i]=width

bowl(oven,d)


#----------------------
def BS(oven,low,high,pizza): #binary search
    mid=-1 # 아래 조건 실행 안되면 0 반환하게끔

    
    ## 찾아야 하는 것: 이 피자가 어디에 위치할 수 있는가?
    while(low<=high): # 등호 조건 0 검사해야해서 필요함
        mid=(low+high)//2
        
        ##못찾음
        if low==high==0 and oven[0]<pizza: #l=h=0으로 하면 0번까지 차있을 때 틀림
            return None
        
        if (oven[mid]>=pizza): #피자 넣을 수 있으면
            if low==high: #같은 경우 - 어차피 low=mid 갱신하면 다음턴에 걸림
                return low  # 아무거나 반환
            
            elif low+1==high: #low, high 1차이나는 경우: low=mid에서 정체될수 있음
                if oven[high]>=pizza: #high 칸(오븐 더 안쪽)에 넣을 수 있는 경우
                    return high
                
                else: #low까지는 넣을 수 있었지만 low 바로 다음칸에는 넣을 수 없음
                    return low
                
            low=mid #작은 쪽으로 이동, mid일땐 되지만 거기서 건너뛰게 되는 경우 존재해서 +1안함

        else: #피자 못넣으면
            high=mid-1
            
    return mid

#----------------------
low=0 # 오븐 너비 큰쪽!! 오븐 상단!!
high= d-1 #작은쪽!!

for i in pizza_d:
    bs_=BS(oven,low,high,i)
    
    if bs_==None:
        print(0)
        sys.exit()
        
    else:
        high=bs_-1 #이미 들어간 자리에는 못들어가므로 -1
        
print(bs_+1) #1부터 시작
