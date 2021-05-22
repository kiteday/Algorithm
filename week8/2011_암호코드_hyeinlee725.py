# 5000자리 이하의 암호(숫자)
code = list(map(int, list(input())))
len_c = len(code) # 암호 길이

# dp[i] : i번째 수 단계에서 암호 코드의 개수
dp = [0 for _ in range(len_c + 1)]
dp[0] = 1 # 가능한 암호
dp[1] = 1 # 첫번째 수로 이뤄진 암호코드는 1개

# 암호를 해석할 수 없는 경우
if code[0] == 0: 
    print(0)
else:
    for i in range(2, len_c + 1):
        # 한자리 수 경우(0 ~ 9)
        if (1 <= code[i - 1] and code[i - 1] <= 9):
            dp[i] += dp[i - 1]
            
        # 두자리 수 경우(10 ~ 26)
        num = code[i - 1] + code[i - 2] * 10
        
        if (10 <= num and num <= 26):
            dp[i] += dp[i - 2]

    # 나올  있는 해석의 가짓수 % 1000000
    print(dp[len_c] % 1000000)
