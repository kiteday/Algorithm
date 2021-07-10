from collections import deque
n=int(input())
nlist=list(map(int,input().split()))

'''
오큰수를 모르고 있는 상태의 index를 스택에 저장
자신보다 큰 수가 나오면 스택에서 꺼내서 그 위치에 nlist 숫자 저장

'''
idx_s=deque() #인덱스 저장용 스택
rs=[-1 for _ in range(n)] #안들어가면 자동으로 -1 들어가게

for idx in range(n):
    while idx_s and nlist[idx_s[-1]]<nlist[idx]:
        rs[idx_s.pop()]=nlist[idx]

    idx_s.append(idx)
    

for a in rs:
    print(a,end=' ') #일렬로 출력
    
