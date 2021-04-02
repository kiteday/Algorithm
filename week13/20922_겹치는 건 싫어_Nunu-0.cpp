#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
	int n, k; // n = 수열의 길이, k = k개 중복이하,
	int temp, length = 0, maxi = 0; // cnt = 연속 수열 길이 maxi = 최장 연속 부분 수열 길이
	int cnt[200001] = {}; // 숫자당 중복 개수
	vector <int> num; // 수열

	cin >> n >> k;

	// 입력하기
	for (int i = 0; i < n; i++) {
		cin >> temp;
		num.push_back(temp);
	}

	int s = 0, e = 0; // 수열의 시작과 끝
	while (s <= e) {
		if (e >= n) {
			if (length <= maxi) // 끝까지 온 상태에서 s가 줄어들면서 length가 늘어나지 않음
				break; // while 탈출
			else {
				cnt[num[s]]--;
				s++;
				length--;
				maxi = max(length, maxi); // 최장 연속 부분 수열 구하기
				continue;
			}
		}

		cnt[num[e]]++; // 중복 개수 카운트
		length++; // 수열 길이
		e++; //수열 길이 1칸 늘어나기

		if (cnt[num[e - 1]] > k) { // 중복 가능회수를 넘겼나
			while (cnt[num[e - 1]] > k) {
				cnt[num[s]]--;
				s++;
				length--;
			}
		}
		else
			maxi = max(length, maxi); // 최장 연속 부분 수열 구하기
	}

	cout << maxi;

	return 0;
}
