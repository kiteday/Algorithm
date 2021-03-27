a,b=map(int,input().split())
cnt=0 #연산 횟수 count
 
while(b!=a): #같으면 종료

    if b%10==1 and b!=1: #마지막 한자리 숫자 검사
        ## 끝자리가 1이면 2로 안나누어떨어질 것 ->1제거
        b//=10 #끝 1자리 제거
        cnt+=1 #연산 횟수 추가



    elif b%2==0: #2로 나누어떨어짐
        b=b//2
        cnt+=1
        
    else: #안됨
        cnt=-2 #+1할거라서 -1출력위해 -2로 설정
        break
    
print(cnt+1) # 연산에 최솟값에 1을 더한 값 출력
    
