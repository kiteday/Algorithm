def solution(skill, skill_trees):
    answer = len(skill_trees) #전체 스킬트리 길이에서 안되는걸 뺄 예정
    skill_len=len(skill) #스킬순서 길이
    
    for t in skill_trees:  #검사
        last_idx=-10 #가장 최근 등장한 인덱스
        for s in skill: # 선행 스킬부터 검사
            '''
            없으면 -1 나옴
            -1이 나오기 전까지 증가하는 형태여야함
            -1이 나온다면 그 뒤로는 다 -1이어야함
           '''
            idx=t.find(s)
            if last_idx==-1: #마지막에 나온 인덱스가 -1이었을 경우
                if idx!=-1:#이후 인덱스가 -1이 아니라면 
                    answer-=1
                    break #가까운 for문 탈출, 다음 loop로
                else: #-1임
                    pass #계속 실행
                
            else: #마지막에 나온 인덱스가 -1이 아님
                if idx==-1: #현재 나온 인덱스가 -1임
                    last_idx=idx
                    
                elif last_idx<idx: #last index보다 현재 나온게 이후에 주어짐
                    last_idx=idx #last_idx 갱신
                    
                else:
                    answer-=1 #현재 나온게 더 작으면 안됨
                    break #가까운 for문 탈출, 다음 loop로
    return answer
