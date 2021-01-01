n = int(input())

stair = [[0 for i in range(10)] for j in range(101)]
#0~9로 시작하는 숫자 * 100번째 자리까지 자연수를 담는 리스트

stair[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# 리스트의 시작

for i in range(2, 101): #1부터 100까지 자연수
    for j in range(10): # 0~9로 시작하는 숫자
        if 1 <= j <= 8: # j-1, j+1
            stair[i][j] += stair[i - 1][j - 1]
            stair[i][j] += stair[i - 1][j + 1]        
        elif j == 0: # i-1, j+1
            stair[i][j] += stair[i - 1][j + 1]
        elif j == 9: # i-1, j-1
            stair[i][j] += stair[i - 1][j - 1]
        
print(sum(stair[n]) % 1000000000) # 1부터 9까지 합에서 1000000000로 나눈 나머지를 출력
