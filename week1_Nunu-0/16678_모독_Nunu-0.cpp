#include <iostream>
#include <algorithm>
using namespace std;
//[16678] 모독
/*
	프로젝트 "Defile"을 실행하려면
	국회의원에 명예 점수가 1부터 오르막 수가 돼야한다.
*/
int main() {
	int n, p = 1; // p = 오르막 수의 위치
	long hacker = 0;
	cin >> n;
	int *honer = new int[n];

	for (int i = 0; i < n; i++) { // 명예 점수 등록
		cin >> honer[i];
	}

	sort(honer, honer + n); // honer[n] 안의 수 정렬

	for (int i = 0; i < n; i++) {
		if (honer[i] >= p) {
			hacker += honer[i] - p; // 명예점수와 바뀔 오르막수의 차
			p++;
		}
	}
	cout << hacker;

	return 0;
}
