import sys
from collections import deque

D, N = map(int, sys.stdin.readline().split())
oven = list(map(int, sys.stdin.readline().split()))
#피자는 차례로 꺼내서 오븐에 넣을꺼니까 데크로 선언
pizza = deque(map(int, sys.stdin.readline().split()))

'''
오븐은 하단 깊은 곳으로 갈수록 좁아지는 형태만 가능함
(어차피 오븐하단에 상단보다 넓은 구역이 있어봤자 사용못하니까)
--> 오븐 하단이 상단보다 큰값일 경우, 상단과 같은 값으로 바꿔줌
'''
for i in range(1, len(oven)):
    if oven[i] > oven[i-1]:
        oven[i] = oven[i-1]
    

def MakingPizza():
    idx = len(oven)-1
    
    while len(pizza) != 0:
        flag = False #오븐에 피자가 들어갈수 있는지 없는지 검사하는용
        piece = pizza.popleft()
        
        for i in range(idx, -1, -1): #오븐 하단에서부터 역순으로 검사
            if oven[i] >= piece: #오븐의 특정 구역에 피자가 들어갈 수 있는 경우
                idx = i-1 #다음에 넣을 피자는 그 구역 위부터 검사하면 됨
                flag = True
                break
        if flag == False: #피자가 모든 오븐 지름보다 큰 경우(아무데도 못들어가는 경우)
            return 0
    
    #반복문 위해 idx=i-1했던거 다시 더해주고, 오븐최상단이 1로 시작하니까 또 1더해줌
    return idx+1+1

print(MakingPizza())