def solution(clothes):
    coustume_type = {}
    # 의상 type 별 개수 구하기
    for i in clothes:
        if i[1] in coustume_type:
            coustume_type[i[1]] += 1
        else:
            coustume_type[i[1]] = 1

    # 조합 구하기
    # 각 개수 + 1 한 값을 전부 곱하기
    if len(coustume_type) == 1:
        return list(coustume_type.values())[0]
    else:
        answer = 1
        for i in list(coustume_type.values()):
    	    answer *= (i + 1)
    	    
    # 아무것도 입지 않은 경우 제외(-1)
    return answer - 1
