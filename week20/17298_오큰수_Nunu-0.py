# [17298] 오큰수
N = int(input())
num = list(map(int, input().split())) # 수열 입력
rst = [-1 for _ in range(N)] # 결과
stack = [] # 스택에는 num안의 순서를 넣는다

for i in range(N):
    # 스택이 비어있지 않다 And 현재 숫자가 스택의 마지막 숫자보다 크다
    while stack and num[i] > num[stack[-1]]:
        rst[stack.pop()] = num[i]
        # stack.pop() = 가장 위 인덱스 빼기, num안의 순서(위치) 반환
    stack.append(i)

print(*rst)