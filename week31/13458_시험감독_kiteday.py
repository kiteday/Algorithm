
N = int(input()) #시험장 수
room=[] #각 시험장의 응시자 수
room = list(input().split())
B, C = map(int, input().split()) #B는 한 번에 총감독관이 감독할 수 있는 응시자 수. C는 부감독
sum = N #필요한 감독관 수 (필요한 총감독관 수로 초기화. 총감은 각 시험장마다 한 명)

for i in range(0,N) :
    num = (int)(room[i])-B
    sum += num//C
    if((num%C) >0) :
        sum+=1

print(sum)