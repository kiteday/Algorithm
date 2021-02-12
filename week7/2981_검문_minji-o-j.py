from math import gcd
import math

n=int(input()) # 숫자의 개수
nlist=[] #숫자 list
m_list=[] #nlist에서 숫자들의 차이 저장하는 집합
for _ in range(n):
    nlist.append(int(input())) #n개의 숫자 입력받음


'''
>유클리드 호제법
어떤 숫자 n[i](정렬된 배열)을 m으로 나누었을 때 나머지 r --> n[i]=m*Q[i]+r
나머지를 없애려면 --> n[i]-n[i-1]=m*(Q[i]-Q[i-1])+(r-r)

> 따라서 위의 식이 성립하기 위해서는
오름차순으로 정렬 한 이후
n[i]-n[i-1]을 저장한 집합의 최대공약수를 구함(m)
최대공약수의 집합에서 약수를 구한 후 정렬 (m의 약수들)
'''

nlist.sort() # 오름차순으로 정렬

for i in range(0,n-1):
    m_list.append(nlist[i+1]-nlist[i]) #차이 저장한 집합 생성
    #m_list.append(nlist[i]-nlist[i+1] if nlist[i]>nlist[i+1] else nlist[i+1]-nlist[i]) #파이썬에서의 삼항연산자 #정렬했으므로 불필요



## 최대공약수 구하기
len_m=len(m_list)

if len_m>=2: #숫자 2개 이상일때 (1개이면 구할 필요 X)
    gcd_=gcd(m_list[0],m_list[1])
    
else: #m이 하나 이상 존재하므로 길이 0이진 않을듯..
    gcd_=m_list[0]

if len_m>2: #2보다 크면 모든 수에 대한 최대공약수 구해야함
    for i in range(2,len_m):
        gcd_=gcd(gcd_,m_list[i]) #현재 최대공약수와 m_list 숫자의 최대공약수 판별


## 최대공약수의 약수 구하기
factor_list=[] #약수 list

for p in range(2,int(math.sqrt(gcd_))+1):
    if gcd_%p==0: #나누어 떨어짐
        a=p
        b=gcd_//p
        
        if a==b: #제곱수
            factor_list.append(a)
        else:
            factor_list.append(a)
            factor_list.append(b)
        
    else:
        continue

if gcd_ not in factor_list:
    factor_list.append(gcd_) #자기 자신 포함
factor_list.sort()

for f in factor_list:
    print(f)
