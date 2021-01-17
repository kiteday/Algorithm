#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
// [18113] 그르다 김가놈
// 시간 절약을 위해 이분탐색 사용

int n, k, m, l, maxi, p = -1; // n = 김밥의 개수, k = 꼬다리의 길이, m = 김밥조각의 최소 개수, l = 김밥 길이, max = 자를수있는 길이 최대, p = 김밥조각의 최대 길이
vector <int> L; // 각 김밥의 길이

int count(int p) {
	int cnt = 0; // Pcm로 자른 김밥의 개수

	for (int i = 0; i < n; i++) {
		if (L[i] >= k * 2) { // 꼬다리 2개 자를 수 있는 길이라면
			cnt += (L[i] - k * 2) / p;
		}
		else if(L[i] > k) { // 꼬다리 1개만 자를 수 있는 길이라면 (2개 자를 길이가 x)
			cnt += (L[i] - k) / p;
		}
	}

	return cnt;
}

void BS(int l, int r) {
	int mid = (l + r) / 2; // 김밥조각의 길이(P)

	if (l > r) { // 중간값(김밥의 길이 P)를 찾거나 없다면 BS 탈출
		return;
	}
	if (count(mid) >= m) { // 최소개수 이상 김밥을 mid센치로 잘랐다는걸 count함수로 확인했다면
		p = max(p, mid);
		BS(mid + 1, r); // 최대 길이를 찾아야하기 때문에 mid보다 긴 길이로 이분탐색
	}
	else {
		BS(l, mid - 1); // 김밥이 안잘렸으므로 mid보다 작은 길이로 이분탐색
	}

}

int main() {

	cin >> n >> k >> m;
	for (int i = 0; i < n; i++) { // 김밥의 길이 입력
		cin >> l;
		L.push_back(l);
		maxi = max(maxi, L[i] - k); // 가장 긴 김밥의 길이 구하기 (꽁다리 한쪽 제거)
	}

	BS(1, maxi); // 1 ~ maxi 길이 만큼 이분 탐색

	cout << p;
}
