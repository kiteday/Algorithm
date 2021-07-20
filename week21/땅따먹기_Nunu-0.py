# [프로그래머스] 땅따먹기
def solution(land):
    answer = 0

    for i in range(1, len(land)): # 세로
        for j in range(len(land[i])): # 가로
            maxi = 0
            for k in range(len(land[i - 1])):
                if j != k: # 같은 행에 있는 것 빼고 가장 큰 숫자 찾기
                    maxi = max(land[i - 1][k], maxi)
            land[i][j] += maxi 
            
    answer = max(land[-1]) 

    return answer