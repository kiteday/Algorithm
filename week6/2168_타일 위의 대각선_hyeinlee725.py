# 유클리드 호제법 - 최대 공약수 이용
# x*y 크기의 타일을 가로지르는 대각선을 그었을 때,
# 그 선이 지나가는 칸의 횟수는 gcd(x, y) - 1번

def gcd(a, b): # 최대 공약수를 구하는 함수
    if (b == 0): # 만약에 b가 0이면
        return a # a를 반환
    else: # 그렇지 않으면
        # 유클리드 호제법과 재귀호출을 이용하여 최대공약수 반환
        # b와 a와 b의 나머지를 통해 계산
        return gcd(b, a % b)

# 첫째 줄에 가로의 길이 xcm와 세로의 길이 ycm
x, y = map(int, input().split())
       
num = gcd(x, y) # 주어진 수의 최대공약수

print(x + y - num) # 대각선이 그려져 있는 타일의 개수
