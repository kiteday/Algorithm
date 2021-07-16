t=int(input()) #테스트케이스 실행 횟수
for _ in range(t):
    n,k=map(int,input().split()) #n: 정수의 개수, k: 정수 기준
    s=list(map(int,input().split())) #정수 list

    # s정렬
    s.sort()

    # 양 끝 포인터, 비교 기준 선언
    l=0
    r=n-1
    min_=10**8*3+1 #최솟값저장
    cnt=0 #개수 count
    
    # 탐색
    while(l<r):
        now=s[l]+s[r]
        
        ## 두개 합이 k보다 크면 오른쪽 줄임
        if now>k:
            r-=1
            
        ## 두개 합이 k보다 작으면 왼쪽 증가
        elif now<k:
            l+=1
            
        ## 두개 합이 k와 같으면 양쪽 줄임
        else: #now==k
            r-=1
            l+=1

        
        ## 두개 더한것과 k와의 차가 최소이면 기준값 갱신
        minus=k-now
        minus=minus if minus>0 else (-1)*minus #양수로 바꾸기
        
        if minus<min_: #차가 최소
            min_=minus #갱신
            cnt=1 #방금것 추가
            
        elif minus==min_:
            cnt+=1 #개수 추가
            
    print(cnt)
        
