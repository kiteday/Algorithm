import sys
input = sys.stdin.readline

def S_of_Eratosthenes(n): # 에라토스테네스의 체
    check = [True for _ in range(n)] # ckeck할 list
    # 시간 단축을 위해 2부터 n의 제곱근까지만 for문 돌림
    for i in range(2,int(n ** 0.5)):
        # 수가 지워지지 않고, 가장 작은 수라면
        if check[i] == True:
            # i의 2배수부터 범위 끝까지 지움
            for j in range(i * 2 , n, i): 
                check[j] = False
    return check

num = S_of_Eratosthenes(1000000)

# Input이 에라토스테네스의 체에 속하면(소수이면)
while True:
    # Input: 테스트 케이스(테스트 케이스의 개수는 100,000개를 넘지 않음)
    T = int(input())
    
    if T == 0 :
        break
    # 소수의 합으로 나타낼 수 있는지 check
    check = False

    # 뒤에 있는 값은 앞에서 이미 검사했을 것으므로 3부터 절반만 검사
    for i in range(3, T // 2 + 1):
        if (num[i] and num[T - i]):
            # n = a + b 형태로 출력
            print("%d = %d + %d"%(T , i , T - i))
            # 소수의 합으로 나타낼 수 있으므로 True로 변환
            check = True
            break

    # 두 홀수 소수의 합으로 n을 나타낼 수 없는 경우
    if (not check): # check == False
        print("Goldbach's conjecture is wrong.")
