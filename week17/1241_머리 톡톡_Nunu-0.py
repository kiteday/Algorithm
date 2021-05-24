import sys
import math
# [1241] 머리 톡톡
def PrimeNum(n): # 약수 구하기
    rst = 0
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0 :
            rst += cnt[i]
            if n / i != i: # 루트를 사용하기 때문에 루트 이상의 숫자인 n / i 도 더해준다. 중복 방지를 위해 if문 사용
                rst += cnt[int(n / i)]
    return rst

N = int(input()) # 학생 수
HeadN = [int(input()) for _ in range(N)] # 머리에 쓴 숫자 # list(map(int,input().split()))
result = [0] * N# 머리를 친 개수
cnt = [0] * (max(HeadN) + 1)

for i in range(N): # 입력 받은 수의 개수 세기
    cnt[HeadN[i]] += 1

for i in range(N): # 머리를 치기
    result[i] = PrimeNum(HeadN[i]) - 1 # -1은 자기자신 빼기
    print(result[i])
        
