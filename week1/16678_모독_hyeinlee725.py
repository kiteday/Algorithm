n = int(input()) #국회의원 명수, 국회의원 명예 점수
honor_score = [] #명예 점수 저장용 배열

#명예 점수 배열에 저장
for i in range(n):
    honor_score.append(int(input())) 

score = 1 #1부터 명예점수를 높여가면서 몇 번의 행동을 취해야하는지 살펴보고
hakers = 0 #해커의 수

for j in sorted(honor_score): #sorted 함수로 오름차수로 정렬
    # print(honor_score)
    if j >= score:
        hakers += j - score # 고용해야할 해커 
        score += 1 # 오름차순으로 반환하기 위해 1을 추가함
        #print(score)

print(hakers) #최소한으로 고용해야하는 해커의 수를 출력
