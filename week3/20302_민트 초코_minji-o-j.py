import sys
from sys import stdin #속도 줄이기용
import math #루트 사용하기 위함

n=int(stdin.readline())
input_=stdin.readline().split()#read line
op=-1 #operator, 0일때 곱셈, 1일때 나눗셈 할 예정
pf={} # 소인수 관리 딕셔너리

'''
1) 순차적으로 계산하니까 틀렸다고 뜸 -> 어딘가에서 손실이 있는건가...?
2) 손실 값 없도록 분자/분모 나눠서 계산 -> 틀렸다고 뜸 -> 오히려 1)보다 더 빨리 틀렸다고 뜨는 것으로 보아 큰 수 계산 오류가 있는 것 같음
3) 소수의 곱으로 나누어 숫자를 표현, 분자/분모에서 각 소수의 개수를 count한다
 - 3-1: 에라토스테네스의 체 이용하여 100000이하 모든 소수 파악, count -> 오래걸림
 - 3-2: 각각 소인수 분해하여 저장
     - 분자 소인수/분모 소인수 나눠서 계산 ->시간초과
     - 분자/소인수 합쳐서 관리
        - 나누어보는 범위: 2~div(소수?-작은것부터 나누므로..) -> 시간초과
        - 에라토스테네스 체 이용하여 거기에 있는 소수만 이용 -> 시간초과
        - n까지의 소수를 검사하는 것이 아니라 root n까지만 검사함!! & rest검사 --> 시간 100배 이상감소
'''

### 에라토스테네스의 체, 소수 배열 출력
def era_prime(N):
    check, answer = [0 for i in range(N+1)], []
    for i in range(2, N+1):
        if check[i] == 0:
            answer.append(i)
        else:
            continue
        for j in range(i*i, N+1, i):
            check[j] = 1
    return answer


### 소인수 분해 저장 함수, 분자에 값 들어올 때 저장용
def prime_factorization(p,lst):
    rest=p #초기값 지정
    prime_list=era_prime(int(math.sqrt(p))) # 소수 배열
    
    for div in prime_list: # 소수 배열에 있는 것
        if rest%div==0: #나누어진 경우(나머지 0)
            while(1): #몇 개 있을지 모름(8->2가 3개)
                if rest%div!=0:
                    break
                rest//=div #나누어진 몫만 저장
                try:
                    lst[div]+=1
                    if lst[div]==0: #값이 0이면 키값 삭제
                        del lst[div]
                except KeyError: # div라는 소인수가 처음 등장
                    lst[div]=1
        else:
            continue #안나눠졌으면 굳이 아래 거칠 필요 x
            
        if(rest==1 or rest==-1): #1 or -1이 될 때 까지
            break

        
    if rest>1: # rest가 1보다 큰데 남아있는 경우: 소수 처리 안된 것 (ex- 루트10=3.xx 이라 5 검사 못해서 rest=5)
        try:
            lst[rest]+=1
        except KeyError:
            lst[rest]=1

    return lst


### 소인수 분해 빼기 함수
def prime_factorization_m(p,lst):
    rest=p #초기값 지정
    prime_list=era_prime(int(math.sqrt(p))) # 소수 배열
    
    for div in prime_list: # 소수 배열에 있는 것
        if rest%div==0: #나누어진 경우(나머지 0)
            while(1): #몇 개 있을지 모름(8->2가 3개)
                if rest%div!=0:
                    break
                rest//=div #나누어진 몫만 저장
                try:
                    lst[div]-=1
                    if lst[div]==0: #값이 0이면 키값 삭제
                        del lst[div]
                        
                except KeyError: # div라는 소인수가 처음 등장
                    lst[div]=-1
        else:
            continue #안나눠졌으면 굳이 아래 거칠 필요 x
            
        if(rest==1 or rest==-1): #1 or -1이 될 때 까지
            break
        
    if rest>1:  # rest가 1보다 큰데 남아있는 경우: 소수 처리 안된 것
        try:
            lst[rest]-=1
        except KeyError:
            lst[rest]=-1
            
    return lst



### 입력 받기
for i in range(2*n-1):
    if i==0: #초기값 설정
        t=int(input_[i])
        if t>0:
            pf=prime_factorization(t,pf) #분자에 추가
        
        elif t==0:
            print('mint chocolate')
            sys.exit(0)
            
        else: #t<0
            pf=prime_factorization(-t,pf)
            
    elif i%2==0: #초기값 이외에 숫자가 들어올 때
        t=int(input_[i])
        
        if op==0: #곱셈
            
            if t==0: #곱셈에 0이 들어간 경우는 무조건 정수 
                print('mint chocolate')
                sys.exit(0)
            elif t>0:
                pf=prime_factorization(t,pf)
            else: #t<0
                pf=prime_factorization(-t,pf)
                
        else: #op=1, 나눗셈
            if t>0:
                pf=prime_factorization_m(t,pf)
            else:
                pf=prime_factorization_m(-t,pf)
                
    else: #i가 홀수일 때: 연산자 입력
        p=input_[i]

        if p=='*': #곱셈 입력
            op=0
        else: #'/'입력
            op=1


'''
분자가 0인 경우는 위에서 끝나므로
소인수 저장 딕셔너리에서 음수인게 있으면 정수 아님
'''
for j in pf:
    if pf[j]<0:
        print('toothpaste')
        sys.exit(0)

print('mint chocolate')
