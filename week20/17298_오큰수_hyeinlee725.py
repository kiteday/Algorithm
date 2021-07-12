import sys

N = int(sys.stdin.readline()) # 수열의 크기
# 수열의 원소
element = list(map(int, sys.stdin.readline().split()))
stack = []
result = [-1 for _ in range(N)]

for i in range(len(element)):
    # 해당 범위 내에 있고, (i < N, stack내에)
    # element[stack[-1]이 element[i]보다 작으면
    while i < N and stack and element[stack[-1]] < element[i]:
        # stack을 pop, result에 element값을 넣어줌
        result[stack.pop()] = element[i]
    # 아니면 i를 stack에 넣어줌
    stack.append(i)
    i += 1
for i in range(N):
    print(result[i], end = ' ')
