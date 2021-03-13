
n,k=map(int,input().split()) #n: 서로 다른 n종류의 인형, k:연속된 인형 선택하는 개수(k개이상)
doll_pref=list(map(int,input().split())) #인형을 선호하는 사람의 수

min_std=10**6 #초기값, 최소의 표준편차를 저장

for kk in range(k,n+1): #k~n개까지 선택
    for i in range(0,1+n-kk):
        select_list=doll_pref[i:i+kk] #인형 선택
        mean=sum(select_list)/kk
        var_list=list(map(lambda x: (x-mean)**2,select_list))
        var=sum(var_list)/kk
        std=var**(1/2)
        
        if min_std>std:
            min_std=std #최솟값 저장

print(min_std)
