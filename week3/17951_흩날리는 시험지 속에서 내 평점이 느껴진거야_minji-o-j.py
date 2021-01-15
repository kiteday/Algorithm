import sys
input_=sys.stdin.readline
n,k=map(int,input_().split()) #n: 시험지의 개수, k: 시험지를 나눌 그룹의 수
q_list=list((map(int,input_().split()))) # map를 이렇게 써야지 리스트의 문자열이 int 형태로 바뀐다!
#print(q_list) # 출력 확인용

'''
n,k 최대 100000이라 그룹의 수를 모두 고려하여 경우의 수를 나눌 순 없음(1초 시간제)
low(최소 점수) :0, high(최대 점수):n*20
합의 최소를 이분탐색으로 찾는다. 합의 최소를 넘는 그룹이 k개 이상 있을 때 mid를 갱신한다
'''
low=0
high=n*20
result=-1 # 최대 mid 반환용

while(low<=high):
    mid=(low+high)//2
    #print(low,mid,high)#확인용 
    check_k=0 # k 개수 count
    check_mid=0 # mid를 넘나 안넘나 합을 계산하기 위함
    
    for i in range(n):
        check_mid+=q_list[i]
        
        if check_mid>=mid: # mid보다 같거나 커지면
            check_mid=0 # 갱신을 위해 다시 0으로
            check_k+=1 # k 개수 만족하는지 확인하기 위하여 반복

        else:
            continue #아래 체크 할 필요 없음

        if check_k>=k: #찾고자 하는 k의 개수와 같아지면(or커지면 근데 아마 커지진않을듯?)
            break # mid 갱신하기 위해 for문 끝내기

    
    if check_k>=k:
        if low==mid: #갱신해도 같을 경우 - 종료조건
            break
        result=mid #조건 충족 저장용
        low=mid
        
    else: #check_k<k
        if high==mid: #갱신해도 같을 경우 - 종료조건
            break
        high=mid

print(result)
