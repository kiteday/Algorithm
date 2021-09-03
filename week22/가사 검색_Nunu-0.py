'''
[프로그래머스] 가사 검색
이진탐색
정확성: 25.0
효율성: 75.0
합계: 100.0 / 100.0
'''
from bisect import bisect_left, bisect_right

# ex) proaa ~ prozz 사이의 단어 개수 계산
def count(wordList, left, right): 
    # 만들 수 있는 단어들의 첫번째 위치
    lPos = bisect_left(wordList, left) 
    # 만들 수 있는 단어들의 마지막 위치
    rPos = bisect_right(wordList, right) 
    # 만들 수 있는 단어의 개수 반환
    return rPos - lPos 

def solution(words, queries):
    answer = []
    word = [[] for _ in range(10001)] # 단어의 최대길이 리스트
    reWord = [[] for _ in range(10001)] # 뒤집을 단어 리스트
    
    for w in words:
        # 단어의 길이별로 구분
        word[len(w)].append(w)
        reWord[len(w)].append(w[::-1]) # 단어 리버스
    
    for i in range(len(word)): # 이진탐색을 사용하기 위해 정렬
        word[i].sort()
        reWord[i].sort()
        
    # 매치되는 단어 찾기
    for q in queries:
        # ?로 시작하는 키워드가 아니면
        if q[0] != '?':
            # (같은 길이의 단어들, ?를 a로 바꿈, ?를 z로 바꿈) 
            cnt = count(word[len(q)], q.replace('?', 'a'), q.replace('?','z'))
        # ?로 시작하는 키워드
        else:
            cnt = count(reWord[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?','z'))
        
        answer.append(cnt)
        
    return answer