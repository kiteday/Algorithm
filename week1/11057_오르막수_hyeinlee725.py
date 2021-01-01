n = int(input())

climb = [[0 for i in range(10)] for j in range(1001)]
#0~9로 시작하는 숫자 * 1000번째 자리까지 자연수를 담는 리스트

climb[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# 리스트 시작(초기화)

for i in range(2, 1001): #1부터 1000까지 자연수
    for j in range(10): # 0~9로 시작하는 숫자
        for k in range(j, 10): # 0~9
            climb[i][j] += climb[i - 1][k]
            
print(sum(climb[n]) % 10007)
# 첫번째 줄에 길이가 N인 오르막 수의 개수를 10007로 나눈 나머지 출력
