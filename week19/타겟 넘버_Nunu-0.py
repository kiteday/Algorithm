#[프로그래머스] 타겟 넘버
def DFS(numbers, loc, sum, target): # 배열, 배열 위치, 합, 타겟 넘버
    global answer
    
    if loc == len(numbers): # 마지막 노드라면 dfs 탈출
        if sum == target:
            answer += 1
        return
    
    DFS(numbers, loc + 1, sum + numbers[loc], target) # +
    DFS(numbers, loc + 1, sum - numbers[loc], target) # -

def solution(numbers, target):
    global answer
    answer = 0
    DFS(numbers, 0, 0, target)
    
    return answer