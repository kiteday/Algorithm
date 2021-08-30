'''
[프로그래머스] 스티커 모으기(2)
정확성: 49.7
효율성: 50.3
합계: 100.0 / 100.0
너무 문제 그대로 푼 느낌
'''
def solution(sticker):
    l = len(sticker) # 스티커의 길이
    sum_sticker = [0 for _ in range(l)]

    # 0번째 스티커
    sum_sticker[0] = sticker[0]
    if l == 1:
        return sticker[0]
    
    # 1번째 스티커
    sum_sticker[1] = sticker[1]
    if l == 2:
        return max(sum_sticker)
    
    # 2번째 스티커
    sum_sticker[2] = sticker[0] + sticker[2]
    if l == 3:
        return max(sum_sticker)
    
    # 0번째부터 스티커를 뜯기 시작했을 때
    for loc in range(3, l - 1): # 마지막 검사x
        sum_sticker[loc] = max(sum_sticker[loc - 2] + sticker[loc], sum_sticker[loc -3] + sticker[loc])
    
    # 최대 합 구하기
    answer = max(sum_sticker)
    
    # 1번째부터 스티커를 뜯기 시작했을 때
    sum_sticker[2] = sticker[2]
    sum_sticker[3] = sticker[1] + sticker[3]
    for loc in range(4, l):
        sum_sticker[loc] = max(sum_sticker[loc - 2] + sticker[loc], sum_sticker[loc -3] + sticker[loc])
    
    #최대 합 구하기
    answer = max(answer, max(sum_sticker))
    
    return answer
