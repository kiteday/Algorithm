N,M=map(int, input().split()) #N:행, M:열
lamp=[list(map(int, input())) for _ in range(N)] #램프상태 저장
K = int(input()) #0~1000
tmp, result=[], 0


for i in range(N):
    cnt0 = 0 #0갯수 세기위한 변수
    cnt_row = 0 #동일한 행 개수 세기 위한 변수
    
    for j in range(M):
        if lamp[i][j] == 0:
            cnt0+=1 #0갯수 카운트
    
    #램프를 켤수있는 조건 검사
    if cnt0 <= K and cnt0%2 == K%2:
        for row in range(N):
            
            #해당 행과 패턴이 동일하면 카운트
            if lamp[i] == lamp[row]:
                cnt_row+=1
    
    #최대값으로 update
    result = max(result, cnt_row)
    
print(result)