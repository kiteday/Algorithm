'''
문자열 검색하는 문제에서 입력되는 문자열이 많을 경우 사용
문자열을 Tree구조로 만들어서 빠른 검색이 가능하게 함 (retrieval에서 따옴)
검색어 자동완성, 사전찾기 등에서 사용
설명 참고: https://twpower.github.io/187-trie-concept-and-basic-problem
'''
import sys
sys.setrecursionlimit(10001) #최대 재귀가 1000으로 되어있어서 효율성 4,5 에러 발생

#쿼리에서 넘어온 단어에 대해 trie 생성하는 함수
def trie(words):
    new_trie={}
    for w in words: #단어1개
        c_trie=new_trie #주소 복사
        for a in w: #문자 1개
            if a in c_trie: #현재 trie 아래 이미 존재하는 문자이면
                c_trie=c_trie[a]
                c_trie['cnt'].append(len(w))
            else:
                c_trie[a]={} #트리 하에 문자 딕셔너리 생성 
                c_trie=c_trie[a]
                c_trie['cnt']=[len(w)] #현재 단어 길이 추가
    return new_trie

# 생성된 trie에서 단어 개수를 가져옴
def count_trie(trie,query,length):
    count=0
    if query[0]=='?': #재귀함수 반복 중 '?' 만남(알파벳 등장 끝남)
        return trie['cnt'].count(length) #현재 trie 딕셔너리에서 단어 길이가 같은것 개수 세서 반환 
    elif query[0] in trie: #아직 알파벳임
        count+=count_trie(trie[query[0]],query[1:],length) #현재 trie 하위 trie를 넘김, 단어 다음 글자부터 넘김,현재 단어 길이 넘김
    return count

def solution(words,queries):
    answer=[]
    r_words=[] #뒤집은 단어 배열 저장
    count={} #단어 길이 count한 dict, 길이:개수 형태
    for w in words:
        r_words.append(w[::-1])
        w_len=len(w)
        if w_len in count:
            count[w_len]+=1
        else: #딕셔너리에 없음
            count[w_len]=1
    
    w_trie=trie(words) 
    rw_trie=trie(r_words)
    
    for q in queries:
        if q[0]=='?'and q[-1]=='?': #?로 시작 ?로 끝남
            #길이만 같으면 ok
            if len(q) in count:
                answer.append(count[len(q)])
            else:
                answer.append(0)
            
        elif q[0]=='?': #?로시작
            answer.append(count_trie(rw_trie,q[::-1],len(q))) #뒤집은 것 넣음
            
        else: #q[-1]=='?'
            answer.append(count_trie(w_trie,q,len(q)))
            
    return answer
