from sys import stdin
import math

# 약수 만들기 (직접 나눠주니 시간초과남)
def divisor(n):
    nlist=set([]) #n의 약수 목록
    for i in range(1,int(math.sqrt(n))+1):
        if n%i==0:
            nlist.add(i)
            nlist.add(n//i)
    
    return nlist

    
n=int(stdin.readline()) #학생 수
numdict={} # 친구가 입력한 숫자, 개수 받음
numlist=[] #친구 입력 순서
for i in range(n):
    num=int(stdin.readline()) # 머리에 쓴 숫자 추가
    if num in numdict: #key값 있는 경우
        numdict[num]+=1
    else:
        numdict[num]=1 #새로 등록
        
    numlist.append(num)

hitlist={} 
for i in numdict.keys(): #친구 머리에 있는 수들
    check=0
    dlist=divisor(i) #key의 약수 목록
    for j in dlist: #약수
        if j in numdict: #약수가 친구 머리에 있으면
            check+=numdict[j]
    
    hitlist[i]=check

for i in numlist:
    print(hitlist[i]-1)
