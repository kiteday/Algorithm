#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
// [5911] 선물
int main() {
	int n, b; // n = 친구 수, b = 돈
	int	p, s; // p = 선물 가격, s = 배송비
	int maxi = 0; // 최대 보낼 수 있는 사람 수
	cin >> n >> b;

	vector <pair<int, int>> price; // <선물 가격, 배송비>
	vector <int> sum(n); // 선물 가격 + 배송비 를 넣을 배열

	for (int i = 0; i < n; i++) {
		cin >> p >> s;
		price.push_back({p, s});
	}

	for (int i = 0; i < n; i++) {
		// i번째 선물을 할인 했을 때의 합 구하기
		for (int j = 0; j < n; j++) {
			// sum = 선물가격 + 배송비
			if (i == j) { // 할인 쿠폰을 쓸 경우
				sum[j] = (price[j].first / 2) + price[j].second;
			}
			else { // 쓰지 않을 경우
				sum[j] = price[j].first + price[j].second;
			}
		}

		sort(sum.begin(), sum.end()); // 친구의 선물 가격을 적은 순서대로 나열

		// 가격이 낮은 순서대로 선물사기
		int money = b; // 현재 소유 중인 돈
		int cnt = 0; // 선물을 산 횟수 (몇번째 선물인지)
		for (int j = 0; j < n; j++) {
			money -= sum[j];

			if (money < 0) {// 돈이 -가 되면 while 탈출
				break;
			}

			cnt++;
		}

		maxi = max(maxi, cnt); // 최대 선물 구매 회수 구하기
	}

	cout << maxi;

	return 0;
}
