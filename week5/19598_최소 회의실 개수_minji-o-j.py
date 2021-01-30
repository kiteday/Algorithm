import sys #입력이 많은 문제라 시간이 매우 단축됨 
n=int(sys.stdin.readline()) #n개의 회의
st=[] #시작 시간 저장 배열
end=[] #끝 시간 저장 배열

for i in range(n): #n개 회의 시작/끝시간 입력
    s,f=map(int,sys.stdin.readline().split()) #회의 시작 시간, 회의 끝나는 시간
    st.append(s) 
    end.append(f)

#시작, 끝시간 정렬
st.sort()
end.sort()

'''
정렬
회의실 모두 저장해서 이를 모두 비교 ->타임아웃
입력 방법 변경 -> 타임아웃
--> 나중에 실험해보니 아래 방법으로 해도 sys사용 한게 10배 이상 시간 단축(입력 많아서 그런듯)
---
# 타임라인으로 접근
# 시작하면 +1, 끝나면 -1을 해서 회의실 개수 최댓값을 구한다.

2^31승까지 모든 숫자에서 더하고 뺌->타임아웃
end 최댓값까지 더하고 뺌 ->타임아웃
start,end 원소로 접근하여 계산->Ok

'''

count=0
maxx=0 #최댓값 저장용
i=0 #st(시작시간)배열 인덱스
j=0 #end(끝시간)배열 인덱스

while(i<n): #종료조건: i가 index를 넘어가면 그때 maxx가 최댓값임, 시작시간>끝나는시간 이므로 j 검사 안해도 됨

    if st[i]<end[j]: #회의 시작 count
        count+=1 
        i+=1 
        
    elif st[i]==end[j]: # 회의 시작, 끝 // count+=1 count-=1이 동시에 일어난다.
        i+=1
        j+=1
        
    else: #회의 끝 count
        count-=1
        j+=1
        
    maxx=max(count,maxx)
    
print(maxx)
