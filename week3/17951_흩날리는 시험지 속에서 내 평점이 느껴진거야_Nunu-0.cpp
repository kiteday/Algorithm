#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
// [17951] 흩날리는 시험지 속에서 내 평점이 느껴진거야
int n, k, x, rst; // n = 시험지 개수, k = 그룹 수, x = 맞은 개수
vector <int> paper; // 각 시험지마다 맞은 개수

void BS(int l, int r) { // 점수l ~ 점수r 확인
	int mid = (l + r) / 2;
	int sum = 0, g = 0; // sum = 점수 총합, g = 그룹수

	if (l > r) {
		return;
	}

	for (int i = 0; i < n; i++) {
		sum += paper[i];
		if (sum >= mid) { // 한 그룹의 점수가 mid 이상이 되면 다음 그룹으로 넘어간다.
			g++;
			sum = 0;
		}
	}

	if (g >= k) { // 그룹의 수가 k보다 많으면 mid 점수가 작다는 의미로 mid ~ r 점수를 확인한다.
		rst = mid;
		BS(mid + 1 , r);
	}

	else { // 그룹의 수가 k보다 적으면 mid점수가 크다는 의미로 l ~ mid 점수를 확인한다.
		BS(l, mid - 1);
	}
}

int main() {
	//시간 단축
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n >> k;

	for (int i = 0; i < n; i++) {
		cin >> x;
		paper.push_back(x);
	}

	BS(0, 20 * n); // 0점 ~ 최대 받을 수 있는 점수

	cout << rst;
}
