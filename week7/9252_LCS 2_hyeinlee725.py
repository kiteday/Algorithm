# 두 문자열 - 알파벳 대문자, 최대 1000 글자
str1 = input() 
str2 = input()

# 문자열의 길이 + 1
l1 = len(str1) + 1
l2 = len(str2) + 1
# DP(동적 계획) 문제
# 2차원 DP 활용 - 행 : 첫번째 문자열, 열 : 두번째 문자열
dp = [['' for _ in range(l2)] for _ in range(l1)]

for i in range(1, l1): # 행
    for j in range(1, l2): # 열
        if not i or not j:
            continue
 
        if str1[i - 1] == str2[j - 1]: # 글자가 같다면
            # + str1[i - 1] - DP + 문자
            dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]
        else: # 같지 않다면
            # dp[i - 1][j]와 dp[i][j - 1] 중 길이가 긴 것을 대
            if (len(dp[i - 1][j]) >= len(dp[i][j - 1])):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]

if (len(dp[-1][-1])) == 0: # LCS가 0인 경우
    #dp[l2 - 1][l1 - 1]
    print(0) # 0 출력, 둘째줄 출력 X
else:
    print(len(dp[-1][-1])) # 입력으로 주어진 두 문자열의 LCS의 길이
    print(dp[-1][-1]) # LCS 출력
