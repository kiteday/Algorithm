from sys import stdin #속도 줄이기용
n=int(stdin.readline()) #국회의원 명수, #int(input()) 대신 속도 줄이기 위하여 사용
clist=[] #명예점수 저장용 

# 국회의원 명예점수 list 만들기
for i in range(0,n):
    score=int(stdin.readline())
    clist.append(score) # 명예점수 배열에 저장

clist.sort() # 명예점수 정렬

find=1 # 1부터 오름차순으로 검색
result=0

# print(clist)

for j in range(0,n): #clist 처음~끝까지 검사
    # print(j+1,':',clist[j],find)
    if clist[j]>=find:
        result+=clist[j]-find # 고용해야할 해커
        find+=1 # 오름차순 만들기 위하여 1 추가

print(result)
