import sys

#BFS탐색
def MixingWords():
    l1, l2, l3 = len(s1), len(s2), len(s3)
    
    #길이 먼저 확인
    if l1+l2 != l3:
        return False
    
    #s3에 s1,s2에 없는 문자열이 있다면 바로 no반환
    tmp = list(set(s1+s2))
    for i in s3:
        if i not in tmp: return False
    
    #큐에 인덱스값으로 s1,s2 문자열 방문하면서 검사하기
    queue, visit = [(0,0)], set((0,0))
    while queue:
        x, y = queue.pop(0)
        if x+y == l3: return True
        
        if x+1 <= l1 and s1[x] == s3[x+y] and (x+1,y) not in visit:
            queue.append((x+1, y))
            visit.add((x+1, y))
        if y+1 <= l2 and s2[y] == s3[x+y] and (x,y+1) not in visit:
            queue.append((x, y+1))
            visit.add((x, y+1))
            
    return False



N = int(sys.stdin.readline())
for i in range(N):
    s1, s2, s3 = [],[],[] #데이터셋 돌 때마다 초기화
    f, s, t = sys.stdin.readline().split()
    s1.extend(f); s2.extend(s); s3.extend(t)
    
    if MixingWords():
        print("Data set %d: yes"%(i+1))
    else:
        print("Data set %d: no"%(i+1))
