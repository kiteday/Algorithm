a,b=map(int,input().split())
minn=100000
cnt=0

def bfs(a,cnt):
    global minn
    print(a,b)
    if a>b:
        return
    if a==b:
        minn=min(minn,cnt)
    cnt+=1
    bfs(a*2,cnt)
    bfs(a*10+1,cnt)

bfs(a,1)

if(minn==100000):
    print(-1)
else:
    print(minn)

'''
2 162
8
'''
