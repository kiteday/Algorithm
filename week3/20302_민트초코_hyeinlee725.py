import sys
import math # math.sqrt를 위해
Dessert = sys.stdin.readline #속도 조절용

N = int(Dessert()) # 수식을 이루는 수의 개수 N (1 <= N <= 100,000)

math_ex = [] # 임의의 수식을 저장할 배열
math_ex.extend(list(Dessert().split())) # 임의의 수식 저장

MAX = int(1e5) # 수식을 이루는 정수의 최댓값 100,000
prime_num = [0 for _ in range (MAX + 1)] # 소수의 개수를 담는 배열

num = [] # 수식에서 정수를 저장하는 배열
operator = [] # 수식에서 연산자를 저장하는 배열

for i in range(len(math_ex)): # 수식을 저장한 배열에서
    if i % 2 == 0: # 정수 저장
        num.append(int(math_ex[i]))
    else: # 연산자 저장
        operator.append(math_ex[i])

zero = False # 0의 존재 여부 판단 + 정수인지 판단
rational_num = False # 유리수인지 판단

# 소인수분해를 통한 소수 개수 증감(합성수)
# 해당 연산자 다음에 온 수의 소수 개수를 증감해야함
# 곱셈 - 소수의 개수 추가
def Mul_num(x):
    root = int(math.sqrt(x))
    # 다음에 온 수의 소수 개수를 증가
    for i in range(2, root + 1):
        # 해당되는 숫자의 소수 개수를 증가시키기 위해
        while((x % i) == 0): 
            x //= i # 합성수를 위한 나눗셈
            prime_num[i] += 1 # 소수 개수 증가
    if (x > 1): # 소인수가 1개인 경우
        prime_num[x] += 1 # 소수 개수 증가

# 나눗셈 - 소수의 개수 감소
def Div_num(x):
    root = int(math.sqrt(x))
    # 다음에 온 수의 소수 개수를 감소
    for i in range(2, root + 1):
        # 해당되는 숫자의 소수 개수를 감소시키기 위해
        while((x % i) == 0): 
            x //= i # 합성수를 위한 나눗셈
            prime_num[i] -= 1 # 소수 개수 감소
    if (x > 1): # 소인수가 1개인 경우
        prime_num[x] -= 1 # 소수 개수 감소

for i in range(len(num)):
    # 첫번째는 앞에 연산자가 없으므로 따로 계산
    if (i == 0):
        # 정수와 유리수 판별에 음수는 관계 없으므로 편의상 양수로 변환
        # 모든 정수는 -100,000이상 100,000이하이므로 다음 조건이 필요
        if (num[i] < 0): 
            num[i] *= -1
        # 0인 경우는 정수
        elif (num[i] == 0):
            zero = True
        else: # 첫번째 숫자이므로 소수 개수 증가
            Mul_num(num[i])

    else:
        # 정수와 유리수 판별에 음수는 관계 없으므로 편의상 양수로 변환
        if (num[i] < 0):
            num[i] *= -1
        # 0인 경우는 정수
        elif (num[i] == 0):
            zero = True
        # 연산자가 곱하기면 곱셈 연산, 아니면 나눗셈 연산
        if (operator[i - 1] == '*'):
            Mul_num(num[i])
        else:
            Div_num(num[i])
            
if zero: # 정수이면
    print("mint chocolate") # mint chocolate 출력
else:
    # 모든 수를 소인수분해하고 2 ~ 100,000에서 소수 배열을 순회
    # 이때 그 값이 음수인 경우는 분모에 수가 남으므로 이는 유리수
    # 그 외에는 정수
    for i in range(2, MAX + 1):
        if (prime_num[i] < 0): # 음수인 경우에는 유리수
            rational_num = True
    if rational_num: # 유리수이면
        print("toothpaste") # toothpaste 출력
    else: # 정수이면 mint chocolate 출력
        print("mint chocolate")
