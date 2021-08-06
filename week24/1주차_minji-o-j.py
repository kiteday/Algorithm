def solution(price, money, count):
    ## 변수 선언
    accum_mount=0 #누적 금액
    
    ## 돈 count
    for i in range(1,count+1):
        accum_mount+=i*price

    ## 부족한 금액 계산
    answer=accum_mount-money
    if answer<0: # 부족하지 않으면
        answer=0
        
        
    return answer
