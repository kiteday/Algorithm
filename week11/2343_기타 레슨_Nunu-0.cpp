#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
// [2343] 기타 레슨
int n, m;
vector<int> lesson;

int bs(int l, int r) {
	while (l <= r) {
		int mid = (l + r) / 2; // 임시로 가정한 한 블루레이의 크기
		int cnt = 0; // 블루레이의 개수
		int bSum = 0; // 한 블루레이안의 레슨 길이

		for (int i = 0; i < n; i++) {
			if (bSum + lesson[i] > mid) { // 블루레이 길이를 초과한다면
				bSum = 0;
				cnt++; // 블루레이 개수 추가
			}
			bSum += lesson[i];
		}
		if(bSum != 0) // 마지막에 빠져나올때 블루레이 길이보다 작으면
			cnt++; // 블루레이 개수 추가

		if (cnt <= m) // 블루레이 개수가 m개 이하라면
			r = mid - 1;
		else // 이상이라면
			l = mid + 1;
	}

	return l;
}

int main() {
	int a, sum = 0, maxi = 0;
	cin >> n >> m;

	for (int i = 0; i < n; i++) { // 블루레이 길이 입력
		cin >> a;
		lesson.push_back(a);
		sum += a;
		maxi = max(maxi, a);
	}

	cout << bs(maxi, sum); // 한 블루레이에 (최소 레슨 길이, 최대 레슨길이)

	return 0;
}
