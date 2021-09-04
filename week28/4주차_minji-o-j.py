def solution(table, languages, preference):
    department = {'SI': 0, 'CONTENTS': 0, 'HARDWARE': 0, 'PORTAL': 0, 'GAME': 0}

    # 직무별 언어에 대한 점수 저장
    for team_table in table:
        split_table = team_table.split(' ')
        team = split_table[0]
        score_table = split_table[1:]

        # 점수 계산을 위한 index 반환
        for pref_idx, language in enumerate(languages):
            try:  # 직업군 언어 점수에 존재
                score = (5 - score_table.index(language)) * preference[pref_idx]
                department[team] += score
            except:
                pass
    data = sorted(department.items(), key=lambda x: (-x[1], x[0]))  # 숫자 큰순, 알파벳순
    answer = data[0][0]
    return answer
