import sys

N=int(sys.stdin.readline())
map=[] #지도정보 입력받음
result=[-10e5, 10e5] #결과저장: 0번째는 max, 1번째는 min
dx, dy = [1,0], [0,1] #우,하향 방향으로만 이동

#지도 입력받아서 숫자만 int로 저장하는 함수
def setting():
    for i in range(N):
        line = sys.stdin.readline().split()
        for j in range(N):
            if i%2==0:
                if j%2==0:
                    line[j] = int(line[j])
            else:
                if j%2!=0:
                    line[j] = int(line[j])
        
        map.append(line)
        
        
def explore(x,y,oper,res):
    for i in range(2):
        new_x = x+dx[i]
        new_y = y+dy[i]

        #바둑판 범위 내인지 확인
        if new_x<N and new_y<N:
            
            #연산자의 경우
            if type(map[new_x][new_y])==str:
                explore(new_x, new_y, map[new_x][new_y], res)
                                    
            #숫자의 경우
            else:
                tmp=0
                if oper=='+':
                    tmp = res+map[new_x][new_y]
                elif oper=='-':
                    tmp = res-map[new_x][new_y]
                elif oper=='*':
                    tmp = res*map[new_x][new_y]
                
                if new_x==N-1 and new_y==N-1:
                    result[0]=max(result[0], tmp)
                    result[1]=min(result[1], tmp)
                    return
                
                explore(new_x, new_y, '/', tmp)

setting()
explore(0,0,'/',map[0][0])
print(result[0], result[1])
