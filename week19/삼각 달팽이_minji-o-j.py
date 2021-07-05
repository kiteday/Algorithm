def solution(n):
    rulelist=[[1,0],[0,1],[-1,-1]] # 아래로, 오른쪽으로, 왼쪽위로
    square= [[[] for _ in range (n)] for _ in range(n)] # 빈배열 만들기
    
    # n번 꺾는다, 그리고 n->n-1..이런식으로 줄어들음
    startnum=1
    rule=0
    row,col=-1,0

    for i in range(n,0,-1):
        for j in range(i):
            row+=rulelist[rule%3][0]
            col+=rulelist[rule%3][1]
            square[row][col]=startnum
            startnum+=1
        rule+=1
    
    answer = []
    for i in range(len(square)):
        for j in range(len(square)):
            if square[i][j]:
                answer.append(square[i][j])
            
    
    return answer
