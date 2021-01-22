import sys
from collections import deque

'''
N = 수빈 위치 (start)
K = 수빈동생 위치 (end, 종착점)
하나의 부모노드에서 3개의 자식노드 생성(+1, -1, *2)
트리의 레벨이 곧 최종적으로 구하고자 하는 값임
큐에 레벨 단위로 값이 들어가있어야 함. 하나의 레벨 순환이 끝나면 count+1
'''

N, K = map(int, sys.stdin.readline().split())
cnt = 0 #총 몇초 걸리는지 count
tree = deque([N]) #초기값N 넣어서 큐 선언
visit = [] #이미 방문한 노드 저장할 용도
result = -1 #while 조건문에 사용
MAX = 100000


def Calc():
    for _ in range(len(tree)):
        node = tree.popleft()
        
        #찾으려는 값이 나오면 그값 return하고 함수종료
        if node == K:
            return node
        
        #방문한 적 없는 값만 계산 진행
        if node not in visit:
            visit.append(node)
            
            for i in (node+1, node-1, node*2):
                if i >= 0 and i <= MAX:
                    tree.append(i)
            
    return -1
            

#N >= K이면 -1밖에 못함 (계산할필요X)
if N >= K:
    cnt = N - K
    print(cnt)

else:
    while result != K:
        result = Calc()
        cnt += 1
    print(cnt-1) #마지막에 정답 반환됐을 때 count+1 된거 빼줘야함