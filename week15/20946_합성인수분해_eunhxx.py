import sys

#소수판별
def is_prime_num(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False #소수X
    return True #소수O

#소인수분해
def factor(n):
    pnum=[] #소인수분해 결과 저장 리스트    
    flag=False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            while n % i == 0:
                pnum.append(i)
                if is_prime_num(n//i):
                    pnum.append(n//i)
                    flag=True
                    break
                n//=i
            if flag:
                break

    return pnum

# -------------------------------------------------

N = int(sys.stdin.readline())
result = factor(N)
if len(result) <= 1:
    print(-1)
    
else:
    if len(result)%2 == 0: #짝수
        for i in range(0, len(result)//2):
            print(result[2*i] * result[2*i+1], end=" ")
    else: #홀수
        for i in range(0, (len(result)-3)//2):
            print(result[2*i] * result[2*i+1], end=" ")
        print(result[-1]*result[-2]*result[-3])
