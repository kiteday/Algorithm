n,m=map(int,input().split()) #n: 행개수, m: 열개수

lampdict={} #중복 없애고 개수 세기 위함
for i in range(n):
    a=tuple(map(int,input())) #[0,1]과 같은 숫자 형태로 저장
    try: #key 존재
        lampdict[a]+=1
    except: #key x ->새로 추가
        lampdict[a]=1

k=int(input()) #몇번 동작?

findmax=[]
for i in lampdict.keys():
    cnt0=i.count(0)
    
    if cnt0==k: # 0개수=k이면
        findmax.append(lampdict[i])#이 행은 모두 켤수있음

    '''
    0개수가 k개보다 작아야함
    k가 짝수이면 0개수도 짝수거나(다 1로 바꾸고 하나 껐다 켜서 원래로 바꿈)
    k가 홀수이면 0개수도 홀수여야함(하나 켜고 하나 껐다 켬)
    '''
    elif cnt0<=k and ((k%2==0 and cnt0%2==0) or  (k%2==1 and cnt0%2==1)):
        findmax.append(lampdict[i])#이 행은 모두 켤수있음


if len(findmax):
    print(max(findmax))
else:
    print(0)
