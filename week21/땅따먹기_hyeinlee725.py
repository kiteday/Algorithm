def solution(land):
    answer = 0
    N = len(land)
    dp = [[0] * 4 for _ in range(N)] # 땅 list 정의
    for i in range(4): # land 대입
        dp[0][i] = land[0][i]

    # 현재 행의 점수와 현재 행의 다음 열과 같지 않은 가장 큰 수를 더함
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] += max(land[i - 1][:j] + land[i - 1][j + 1:])
        answer = max(land[len(land) - 1]) # 최대값 반환
    return answer
