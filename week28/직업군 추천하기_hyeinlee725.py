'''
zip : 동일한 개수로 이루어진 자료형을 묶어주는 역할을 하는 Python 내장 함수
'''
def solution(table, languages, preference):
    score = [] # 직업군 언어 점수 저장 list
    # table을 이차원 list로 변경
    new_table = [table[t].split() for t in range(len(table))]
    for i in range(len(new_table)):
        total = 0 # total 점수
        # zip : language와 perference를 묶어줌
        for lan, pref in zip(languages, preference):
            if (lan in new_table[i]):
                # 언어 선호도 * 직업군 언어 점수
                total += pref * (len(new_table[0]) - new_table[i].index(lan))
        score.append(total) # 점수 저장
    job = [] # 직업군 저장 배열
    max_score = max(score) # 가장 선호하는 언어
    for i in range(len(score)):
        if (score[i] == max_score):
            job.append(new_table[i][0])
    job.sort() # 총합이 같은 직업군일 경우, 사전순으로 가장 빠른 직업군
    return job[0]
