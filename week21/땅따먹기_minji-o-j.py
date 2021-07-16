def solution(land):
    row=len(land) #행의 개수
    dp= [[0 for _ in range(4)] for _ in range(row)] #land size의 배열 생성
    
    for i in range(4): #0행 채우기
        dp[0][i]=land[0][i]
    
    for r in range(1,row): #행 반복
        for c in range(4): #열 반복
            dp[r][c]=land[r][c]+max(dp[r-1][:c]+dp[r-1][c+1:]) #현재값+현재 열 제외한 이전 행에서의 최댓값

    answer=max(dp[row-1])
    return answer
