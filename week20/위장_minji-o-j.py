def solution(clothes):
    # 종류 딕셔너리 생성 및 입력
    clothing={}
    for c in clothes:
        try:
            clothing[c[1]].append(c[0])
        except KeyError:
            clothing[c[1]]=[c[0]]
    
    # 각각 개수+1 씩 곱함
    answer=1
    
    for k in clothing.keys():
        answer*=(len(clothing[k])+1)
    
    #모두 선택X경우 제외함
    answer-=1
    
    return answer
