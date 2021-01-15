#include <iostream>
#include <cmath>
using namespace std;
// [20302] 민트 초코
bool zero; // 수에 0이 들어가는 경우
int fac[100001]; // 소인수분해 후 소수가 들어갈 배열

void mul(int n) { // 곱셈이면 n을 소인수분해 후 소수를 배열에서 추가
	for (int i = 2; i * i <= n; i++)
		while ((n % i) == 0) {
			n /= i;
			fac[i]++;
		}
	if (n > 1) {
		fac[n]++;
	}
}

void div(int n) { // 나눗셈이면 n을 소인수 분해 후 소수를 배열에 빼기
	for (int i = 2; i * i <= n; i++)
		while ((n % i) == 0) {
			n /= i;
			fac[i]--;
		}
	if (n > 1) {
		fac[n]--;
	}
}

int main() {
	//시간 단축
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);

	int n, num; // 숫자
	char oper; // 연산자

	cin >> n;

	for (int i = 0; i < n; i++) { // 숫자랑 연산자 입력
		if (i == 0) { // 첫번째로 입력받은 수일때
			cin >> num;
			if (num < 0) { // 음수를 양수로 바꿈
				num *= -1;
			}
			else if (num == 0) {
				zero = true;
			}
			mul(num);
		}
		else {
			cin >> oper >> num;
			if (num < 0) { // 음수를 양수로 바꿈
				num *= -1;
			}
			else if (num == 0) {
				zero = true;
			}

			if (oper == '/') { // 나눗셈일때
				div(num);
			}
			else if(oper == '*') { // 곱셈일때
				mul(num);
			}
		}
	}

	if (zero) {
		cout << "mint chocolate";
		return 0;
	}
	for (int i = 2; i <= 100000; i++) { // 배열안에 음수가 있다면 유리수라는 의미(나누지 못한 수가 남았다)
		if (fac[i] < 0) {
			cout << "toothpaste";
			return 0;
		}
	}
	cout << "mint chocolate";

	return 0;
}
