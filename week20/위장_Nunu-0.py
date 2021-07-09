# [프로그래머스] 위장
def solution(clothes):
    answer = 1
    clothe = dict() # 종류 : 개수
    
    for name, kind in clothes:
        if kind in clothe : # clothe안에 이미 종류가 포함 돼 있다면 개수만 추가
            clothe[kind] += 1
        else : # clothe안에 옷의 종류가 처음 등록된다면 
            clothe[kind] = 1
            
    for value in clothe.values(): # 경우의 수 곱하기
        answer *= (value + 1) # +1은 안입은 경우를 고려
    
    return answer - 1 # -1 로 아무것도 안 입었을 경우를 뺌