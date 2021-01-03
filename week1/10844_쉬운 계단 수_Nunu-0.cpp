#include <iostream>
using namespace std;
//[10844] 쉬운 계단 수
int main() {
	int n, rst = 0, m = 1000000000;
	int N[101][10] = {}; // [자리수][숫자]
	cin >> n;

	for (int i = 0; i < 10; i++) { // 1의 자리수
		N[1][i] = 1;
	}
	for (int i = 2; i <= n; i++) { // 10의 자리수 부터
		for (int j = 0; j < 10; j++) {
			if (j == 0) { // 0과 1차이 나는 수는 1밖에 없음
				N[i][j] = N[i - 1][j + 1];
			}
			else if (j == 9) { // 9와 1차이 나는 수는 8밖에 없음
				N[i][j] = N[i - 1][j - 1];
			}
			else {
				N[i][j] = (N[i - 1][j - 1] + N[i - 1][j + 1]) % m;
			}
		}
	}
	for (int i = 1; i < 10; i++) { // 0으로 시작하는 수는 없음
		rst = (rst + N[n][i]) % m;
	}
	cout << rst;

	return 0;
}
