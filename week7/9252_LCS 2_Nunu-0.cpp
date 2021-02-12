#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
// [9252] LCS 2
int dp[1001][1001]; // LCS를 구하기 위한 배열 (전역변수에 입력하면 0으로 자동 초기화)
// dp를 지역변수에 넣고 = {} 로 했더니 [런타임 에러 (OutOfBounds)] 가 남.. 이유가 뭘까?

int main() {
	string s1, s2; // s1 = 첫번째 문자열, s2 = 두번째 분자열
	string LCS = ""; // LCS 문자 결과


	cin >> s1 >> s2;

	int a = s1.size(); // 첫번째 문자열의 길이
	int b = s2.size(); // 두번째 문자열의 길이

	for (int i = 1; i <= a; i++) { // 행
		for (int j = 1; j <= b; j++) { // 열
			if (s1[i - 1] == s2[j - 1]) { // 글자 모양이 같다면
				dp[i][j] = dp[i - 1][j - 1] + 1; // 1이 늘어남
			}
			else { // 같지않으면 왼쪽 또는 위쪽에서 큰 숫자를 가지고 옴
				dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
			}
		}
	}

	cout << dp[a][b] << endl; // LCS의 길이 출력

	while (dp[a][b] != 0) { // LCS 길이가 0이 될때까지
		if (dp[a][b] == dp[a][b - 1]) {
			b--;
		}
		else if (dp[a][b] == dp[a - 1][b]) {
			a--;
		}
		else {
			LCS = s1[a - 1] + LCS;
			a--;
			b--;
		}
	}

	cout << LCS;

	return 0;
}
