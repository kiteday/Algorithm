# [프로그래머스] 스킬트리
def solution(skill, skill_trees):
    answer = 0

    for i in range(len(skill_trees)):
        pos = 0  # 스킬의 순서 위치
        for j in range(len(skill_trees[i])):
            if (pos < len(skill)) and (skill[pos] == skill_trees[i][j]):
                pos += 1
            elif skill_trees[i][j] in skill:  # 스킬이 순서대로가 아니면 멈춤
                break;

            if len(skill_trees[i]) - 1 == j:  # 정상적으로 스킬을 배웠으면 +1
                answer += 1

    return answer