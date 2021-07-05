def DFS(numlist,target,now,idx):#숫자 배열, 타겟, 현재 숫자,현재 인덱스
    global answer
    
    if idx==len(numlist): # 마지막 index까지 검사했다면
        #print(now)
        if now==target: #타겟 넘버 만들어지면
            answer+=1 #정답 개수 추가
        return

    DFS(numlist,target,now+numlist[idx],idx+1) #현재 위치에 +붙인것
    DFS(numlist,target,now-numlist[idx],idx+1) #-붙인것
    
def solution(numbers, target):
    global answer
    answer=0 #타겟 넘버 개수 count용
    DFS(numbers,target,0,0)
    return answer
