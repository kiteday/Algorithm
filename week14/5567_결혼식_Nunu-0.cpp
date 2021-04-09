#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
//[5567] 결혼식
int main() {
	int n, m; // n = 상근이의 동기의 수, m = 리스트의 길이
	int a, b; // 친구 관계
	int rst = 0; // 초대하는 동기 수

	cin >> n >> m;
	vector<int> friends[501]; // [n]번째 사람의 친구를 넣을 벡터(리스트), 벡터 501개 만든 것
	vector<bool> list(n + 1); // 초대하는 동기 중복 확인, 백터 1개


	// 친구리스트 작성
	for (int i = 0; i < m; i++) {
		cin >> a >> b;
		// 서로의 리스트에 친구 등록
		friends[a].push_back(b);
		friends[b].push_back(a);
	}

	// 초대할 동기수 구분
	for (int i = 0; i < friends[1].size(); i++) { // 상근이의 친구
		int s = friends[1][i]; // 상근이의 친구
		list[s] = true;

		//상근이의 친구의 친구
		for (int j = 0; j < friends[s].size(); j++) {
			list[friends[s][j]] = true;
		}
	}

	// 초대하는 동기수 세기
	for (int i = 2; i <= n; i++) {
		if (list[i] == true)
			rst++;
	}

	cout << rst;

	return 0;
}
