# 유클리드 호제법 - 최대 공약수 이용
import sys
import math # sqrt를 사용하기 위해
Natural_num = sys.stdin.readline # input

# 최대 공약수를 구하는 함수 - 유클리드 호제법
def gcd(a, b):
    if (b == 0):
        return a 
    else: 
        return gcd(b, a % b)

# 약수 구하는 함수
def div(num):
    # 주어진 숫자에서 나머지 없애기
    if num[0] < num[1]:
        m = num[1] - num[0]
    else:
        m = num[0] - num[1]

    ## 약수 구하기 ##
    div_list = [m]
    # 시간 절약을 위해 최대공약수의 제곱근까지만 for문 돌림
    for i in range(2, int(math.sqrt(m)) + 1):
        if m % i == 0: # 나머지가 0이면
            div_list.append(i) # 리스트에 저장
            if m // i != i: # 만약 몫이 i가 아니면
                div_list.append(m // i) # 해당 값 리스트에 저장

    M = [] # 종이에 적은 수를 M으로 나누었을 때, 나머지가 모두 같게 되는 M
    for i in range(len(div_list)):
        r = num[0] % div_list[i] # 나머지 구하기
        for j in range(1, len(num)):
            # 나머지가 같은지 확인
            # 나머지가 다르면 pass
            if r != num[j] % div_list[i]:
                break
            # 모든 나머지가 같으면 list에 추가
            if j == len(num) - 1:
                M.append(div_list[i])
    M.sort() # 리스트 정렬

    return M # 반환

# 종이에 적은 수의 개수 N (2 ≤ N ≤ 100)
N = int(Natural_num())
num = [] # 숫자 저장 list(1보다 크거나 같고, 1,000,000,000보다 작거나 같은 자연수)

for i in range(N): # N개 줄에는 종이에 적은 수가 하나씩 주어짐
    num.append(int(Natural_num())) #
num.sort() # 리스트 정렬

for k in div(num): # 가능한 M을 공백으로 구분하여 모든 M 출력
    print(k, end = ' ')
