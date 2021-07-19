def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        skill_list = []
        check = True
        for j in i:
            # skill_tres 값이 skill에 있으면 skill_list에 추가
            if j in skill:
                skill_list.append(j)
        for l in range(len(skill_list)):
            # 순서가 다르면
            if (skill_list[l] != skill[l]):
                # False 반환, 불가능한 skill tree
                check = False
                break
        # 정상적으로 skill을 배웠으면(순서가 다 같으면) 가능한 skill tree
        if check == True:
            answer+=1
            
    return answer
