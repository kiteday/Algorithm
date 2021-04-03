n,k=map(int,input().split()) #n: 수열의 길이, k: 같은 정수가 k개 이하
a=list(map(int,input().split())) #수열
maxlen=0 #최대 길이 저장
checklist=[0 for i in range(100001)] #같은 정수 길이 체크용, 0으로 초기화

'''
연속된 숫자를 고려하는 문제로 포인터 2개를 움직여서 모든 경우 중 가장 큰 것을 체크하
'''
p1,p2=0,0 #포인터
flag=0 # p1을 늘리면 1, 아니면 0
while(p2<n and p1<n):
    if flag==0:
        checklist[a[p2]]+=1 #숫자 추가


    if checklist[a[p2]]>k: # 새로 추가된 숫자가 같은 정수의 개수 길이 초과하면
        checklist[a[p1]]-=1 #현재 p1에 있는 숫자 제거
        p1+=1 # p1의 포인터 이동
        flag=1

    else: # 초과하지 않으면
        checkmax=p2-p1+1
        if checkmax>maxlen:
            maxlen=checkmax
            
        p2+=1
        flag=0

print(maxlen)
