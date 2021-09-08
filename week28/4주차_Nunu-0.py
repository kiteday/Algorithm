# [프로그래머스] 4주차
def solution(table, languages, preference):
    # 공백으로 나눠져 있던 1차 배열 table을 2차 배열로 바꾸기 
    n_table = [table[i].split(" ") for i in range(5)] 
    score = [0] * 5
    answer = []

    for i in range(5): # table의 열
        for j in range(len(languages)):
            if languages[j] in n_table[i]:
                # i번째 직업군 += 점수 * 선호도
                score[i] += (len(n_table[0]) - n_table[i].index(languages[j])) * preference[j]
    
    # 개발자가 가장 선호하는 언어 
    maxi = max(score)
    for i in range(5):
        if maxi == score[i]:
            answer.append(n_table[i][0])
    # 같은 값인 경우 이름 사전 순
    answer.sort()
    
    return answer[0]
