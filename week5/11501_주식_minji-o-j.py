import sys
t=int(sys.stdin.readline()) #테스트 케이스

#----------------------------
def sell(buy,max_,profit): #팔 주식 배열, 판매할 가격, 이윤 저장
    
    for i in buy:
        profit+=(max_-i) #이윤 계산
        
    return profit

#----------------------------
for _ in range(t):
    n=int(sys.stdin.readline()) # 날의 수
    price=list(map(int,sys.stdin.readline().split())) # 날 별 주가를 나타내는 n개의 자연수

    '''
    price에서 가장 큰 값 미리 알고있는다. 이전 값들은 나오면 다 팔아버린다.
    그리고 그 이후 배열에서 max 새로 구한다. ->시간초과 (O(n^2))
    set배열 바꾼후 max -> 시간초과 (O(n^2))

    #--------
    뒤에서부터 탐색-> 맨 뒤에 값 저장, max_보다 더 작을 경우 살 주식에 추가
    max_보다 클 경우 살 주식 모두 판매, max 갱신
    
    '''
    price=price[::-1] #뒤집기
    max_=price[0] # 맨 뒤의 값(뒤집어서 맨 앞의 값)
    
    buy=[] #구매할 주식
    profit=0 #번 돈
    
    for i in range(1,n): #0은 이미 위에서 저장함
        
        if price[i]<=max_: #작거나 같은 경우 - 살 주식에 추가
            buy.append(price[i])

        else: #새로운 max값 등장
            profit=sell(buy,max_,profit) #판매
            buy=[]
            max_=price[i]

    # buy가 안 비었음 (새로운 max값 등장 안하고 끝남)
    profit=sell(buy, max_,profit)
            
    print(profit)


        
