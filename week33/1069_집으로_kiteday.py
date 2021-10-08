import math

X, Y, D, T = map(int, input().split()) #값 입력 받기
back = math.sqrt(X**2+Y**2) #집까지 거리를 계산
time = 0.0

if(D>back): #1회 점프가 집으로 가는 거리보다 클 때
    if(back < T+(D-back)): #걸어가는 게 빠른 경우
        time += back
    else:
        time += D - back + T #점프해서 집을 지나친 후 다시 돌아오는게 빠른 경우
else:
    jump, walk = divmod(back, D)
    if(jump*T < jump*D):
        time += jump * T
    else: #뛰어가는 것보다 걸어가는게 빠를 때
        time += jump * D
    if (walk >0):
        if(walk < (T + (D-walk))):
            time += walk
        else:
            time += T+(D-walk) #점프해서 집을 지나친 후 다시 돌아오는게 빠른 경우
print(time)