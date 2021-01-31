import sys

T = int(sys.stdin.readline())
result = []

def Greedy(stock):
    #idx: max값 위치의 인덱스 저장. idx까지 profit 계산할 것
    #pre_idx: 이전 루프에서 idx까지 profit 계산했으니까 idx+1부터 새로 계산해야 함
    profit, idx, pre_idx, cnt = 0, -1, 0, 0
    
    while cnt != len(stock):
        pre_idx = idx+1
        max = stock[pre_idx] #max는 항상 시작값으로 초기화
        
        # max값 찾기
        for i in range(pre_idx, len(stock)):
            if max <= stock[i]:
                max = stock[i]
                idx = i
                
        # profit 계산
        for j in range(pre_idx, idx+1):
            profit += (max - stock[j])
            cnt += 1
    
    return profit
    


for _ in range(T):
    stock = []
    N = int(sys.stdin.readline())
    stock = list(map(int, sys.stdin.readline().split()))
    result.append(Greedy(stock))#함수 호출해서 계산하고, 결과를 result배열에 저장
    


for res in result:
    print(res)