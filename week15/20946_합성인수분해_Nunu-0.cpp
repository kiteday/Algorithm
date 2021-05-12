#include <iostream>
#include <vector>
#include <math.h>
using namespace std;
//[20946] 합성인수분해

int main() {
	long long N, n;
	vector <long long> PN; // N의 소인수분해
	cin >> N;

	for (long long i = 2; i <= sqrt(N); i++) { // N 소인수분해
		if (N % i == 0) {
			PN.push_back(i);
			N /= i;
			i = 1;
		}
	}
	PN.push_back(N);

	if (PN.size() <= 1) //합성수가 하나도 없을 때
		cout << -1;
	else {
		for (int i = 0; i < PN.size() / 2; i++) {
			n = PN[i * 2] * PN[i * 2 + 1];
			if (i * 2 + 3 == PN.size()) // 홀수인 경우
				n *= PN[i * 2 + 2];
			cout << n << " ";
		}
	}

	return 0;
}
