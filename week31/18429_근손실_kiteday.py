from itertools import permutations

N, K = map(int, input().split()) #N은 운동키트 수, K는 중량감소량
kit = list(input().split()) #각 키트의 중량
_kit = list(permutations(kit, N)) #키트가 가질 수 있는 경우의 수

cnt = len(_kit) #키트의 모든 조합 수
for i in _kit :
    W =500
    for j in i:
        #print(j)
        j = int(j)
        W = W-K + j
        if W >= 500:
            pass
        else :
            cnt -=1 #조건에 충족하지 않으면 감소
            break
#처음에는 반대로 조건에 충족하면 증가로 코드를 짜보았으나 파이썬 결과는 제대로 나오는데 백준에서 틀렸다고 나온 것을 보아 틀린 내용이 있었나봄..!
print(cnt)

