#include <iostream>
using namespace std;
//[11057] 오르막 수
int main() {
	int N[1002][10] = {}; //[자리수][숫자]
	int n, rst = 0;
	cin >> n;

	for (int i = 0; i < 10; i++) { // 1의 자리수 초기화
		N[1][i] = 1;
	}
	for (int i = 2; i <= n + 1; i++) { // n의 자리수
		for (int j = 0; j < 10; j++) {
			for (int k = j; k < 10; k++) { // j보다 큰 수
				N[i][j] = (N[i][j] + N[i - 1][k]) % 10007;
			}
		}
	}
	cout << N[n + 1][0] % 10007;

	return 0;
}
