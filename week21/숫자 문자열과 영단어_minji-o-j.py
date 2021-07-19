import re
def findnum(s,numstr,num):
    while True: 
        searchobj=re.search(numstr,s) #찾기, 문자열 시작 index와 끝 index 반환
        
        if searchobj:
            start,end=searchobj.span()
            if start>0: #맨 앞에 있는게 아니라면
                changestr=s[:start] #뒤에 연결
                
            else: #맨 앞에 있으면
                changestr=str()

            changestr="".join([changestr,str(num)]) #str형태는 append말고 join사용해야함
            changestr="".join([changestr,s[end:]])
            s=changestr
        else:
            return s #if문 만족 못할 경우
        
def solution(s):
    # 문자열 없이 그냥 숫자일 경우
    try:
        answer=int(s)
        return answer
    
    # 문자열 포함할 경우
    except ValueError: #int변환 불가
        #1부터 순서대로
        s=(findnum(s,'zero',0))
        s=(findnum(s,'one',1))
        s=(findnum(s,'two',2))
        s=(findnum(s,'three',3))
        s=(findnum(s,'four',4))
        s=(findnum(s,'five',5))
        s=(findnum(s,'six',6))
        s=(findnum(s,'seven',7))
        s=(findnum(s,'eight',8))
        s=(findnum(s,'nine',9))
        return int(s)

        
        
