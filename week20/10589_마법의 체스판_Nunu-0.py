# [10589] 마법의 체스판
n, m = map(int,input().split())
# 행 먼저 짝수줄을 바꾸고 열의 짝수줄을 바꾼다

print (n // 2 + m // 2) # 반전 횟수

for i in range(1, n // 2 + 1): # 행 짝수줄
    print(i * 2, 1, i * 2, m) # 세로로 긴 직사각형
for i in range(1, m // 2 + 1): # 열 짝수줄
    print(1, i * 2, n, i * 2) # 가로로 긴 직사각형