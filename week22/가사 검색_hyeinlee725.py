'''
*Trie 구조*
*문자열을 tree 형태로 저장하고 효율적으로 탐색하는 자료구조
*root에서부터 자식들을 따라가며 생성된 문자열들이 Trie 자료구조에 저장
*Node : 3가지가 필요 - key(값으로 입력될 문자열), count(단어 개수), children(자식 노드)
*Trie : 여러가지 함수 필요 - head를 빈노드로 설정, insert 함수(tree 생성 함수),
         search 함수(문자열 존재 여부 return하는 함수 - data 존재시 True, 아니면 False),
         starts_with 함수(단어를 찾고 배열로 return 하는 함수 - data 존재하는 것만 저장)
         -> 해당 문제는 숫자로 결과를 나타내무로 search와 starts_with 함수를 합쳐서 사용
'''
# defaultdict : 사전 기본 값으로 dict를 생성할 때 기본적으로 Trie형태로 생성하기 위해 호출
from collections import defaultdict

class Node(object):
    def __init__(self, key):
        self.key = key 
        self.count = 0
        self.children = {}
        
class Trie(object):
    def __init__(self):
        self.head = Node(self) # 최상위 node 생성

    def insert(self, string): # tree 생성 함수
        cur_node = self.head # 최상위 node 호출
        for char in string: # 입력받은 단어 한글자씩 반복
            cur_node.count += 1
            if (char not in cur_node.children): # 해당 단어가 없으면
                cur_node.children[char] = Node(char) # 자식 노드 생성
            cur_node = cur_node.children[char]
        cur_node.count += 1 # count + 1(새로 추가된 자식 노드, 단어 개수)

    def starts_with(self, prefix):
        cur_node = self.head # 최상위 node 호출
        for p in prefix:
            if (p == '?'): # ?가 있는 경우
                break # 반복문 종료
            if (p in cur_node.children): # 단어 p가 있으면
                cur_node = cur_node.children[p] # children node로 이동
            else: # p not in cur_node.children
                return 0
        return cur_node.count

def solution(words, queries):
    answer = []
    trie = defaultdict(Trie)
    reverse_trie = defaultdict(Trie) # Trie를 reverse하게 생성
    for w in words: # words를 insert
        trie[len(w)].insert(w)
        reverse_trie[len(w)].insert(w[::-1])
    
    for q in queries:
        if (q[0] != "?"): # 첫 문자가 "?"가 아닌 경우
            res = trie[len(q)].starts_with(q)
        else: # "?"인 경우
            res = reverse_trie[len(q)].starts_with(q[::-1])
        answer.append(res)
    return answer
