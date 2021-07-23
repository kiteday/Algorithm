def solution(words, queries):
    answer=[]
    for i in queries:
        alphaindex=[] #알파벳이 있는 곳의 index를 저장
        count=0
        for j in range(len(i)):
            if i[j].isalpha():
                alphaindex.append(j)
        
        for w in words:
            if alphaindex: #숫자존재 
                if w[alphaindex[0]:alphaindex[-1]+1]==i[alphaindex[0]:alphaindex[-1]+1] and len(w)==len(i):
                    count+=1
            else: #다 물음표
                if len(w)==len(i):
                    count+=1
                
        answer.append(count)
    return answer
