'''
[프로그래머스] 보석 쇼핑
정확성: 33.3
효율성: 66.7
합계: 100.0 / 100.0
'''
def solution(gems):
    answer = [] 
    gems_cnt = {} # {구매한 보석의 종류 이름 : 개수}
    start, end = 0, 0 # 시작점, 끝점
    min_len = len(gems) + 1 # 최단 구간 길이
    gems_kind = len(set(gems)) # 보석의 종류 개수 (변수로 따로 만들지 않으면 효율성 0점 나옴)
    
    while end < len(gems):
        # 구매한 보석 개수 카운트하기
        if gems[end] not in gems_cnt: # 처음 구매하는 보석이면
            gems_cnt[gems[end]] = 1 # dic에 추가
        else: # 구매한 적이 있다면
            gems_cnt[gems[end]] += 1 # 기존에 +1

        # 모든 보석을 구매했을 때
        while len(gems_cnt) == gems_kind:
            # 중복으로 구매한 보석일 경우 사지 않고 시작 지점을 오른쪽으로 한칸 옮긴다 
            if gems_cnt[gems[start]] > 1:
                gems_cnt[gems[start]] -= 1
                start += 1
            # 최단 길이 갱신
            elif min_len > end - start:
                min_len = end - start
                answer = [start + 1, end + 1]
                break
            # 최단 거리가 아니면 멈춤
            else:
                break
        
        # 다음 보석 구매
        end += 1 

    return answer
