import sys
import math
n=int(input()) #n은 2보다 큼
resultlist=[]

def isprime(n): #소수판별
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True


def prime(n): #소수 분해
    primelist=[]
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            while n%i==0:
                primelist.append(i)
                
                if (n//i)>math.sqrt(n) and isprime(n//i): #나누고 몪이 소수일때

                    primelist.append(n//i)
                    n=n//(n//i)
                n//=i
                
    return primelist

resultlist=prime(n)
#print(resultlist)
lenlist=len(resultlist)
if lenlist==0 or lenlist==1: #길이 0이면
    print(-1)

elif(lenlist%2==0): #길이 짝수면 ->2개씩 묶음
    for i in range(0,lenlist//2):
        print( resultlist[i*2]*resultlist[i*2+1],end=' ')

else: #길이 홀수개 ->2개씩, 마지막만 3개 묶음
    for i in range(0,lenlist//2-1):
        print(resultlist[i*2]*resultlist[i*2+1],end=' ')
    print(resultlist[-1]*resultlist[-2]*resultlist[-3])
