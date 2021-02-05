#include <iostream>
using namespace std;
// [2168] 타일 위의 대각선
int gcd(int x, int y) { // 유클리드 호제법

	return !y ? x : gcd(y, x % y);
	// 두번째 숫자가 0이 될때까지 x & y를 반복해서 최대 공약수를 구함
	// y = 0 일때 x = 최대 공약수
}

int main() {
	int x, y;

	cin >> x >> y;
	// g = 최대 공약수
	// g (x / g + y / g -1) = x + y - g
	cout << x + y - gcd(x, y);

	return 0;
}
