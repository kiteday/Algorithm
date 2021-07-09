# 행, 열
n, m = map(int,input().split())

# 반전 횟수 k
k = n//2 + m//2
print(k)

# 직사각형의 모서리를 포함하는 좌표
# 하나 건너 뛰어서 반전시키면 최소한으로 모든 칸의 색상이 같게할 수 있음
for i in range(2, n + 1, 2):
    print(i, 1, i, m)
# 마주보는 모서리의 좌표
for j in range(2, m + 1, 2):
    print(1, j, n, j)
