#include <iostream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;
// [1089] 스타트링크 타워
/*
	아래와 같은 숫자가 나올 수 없는 경우가 나오면
	시스템 종료
	|...|
	|.#.|
	|...|
	|.#.|
	|...|

	평균값을 구할 때 모든 경우의 수를 구한다면 시간오바
	>> 자리수 마다의 평균을 구해 더하면 평균값이 나옴
	ex ) avg(a,b,c)*10 + avg(a,b,c,d)
*/

int n;
string input[5]; // 입력한 모양
string number[10]; // 입력한 모양을 한줄로 바꿔 저장할 배열
string shape[10]; // 숫자 모양
vector <int> num[10]; // 매 번호판 마다 들어갈 수 있는 숫자 저장
double result = 0;

// 번호판과 비교해 가능한 숫자를 체크하는 함수
void check(int x) {
	for (int i = 0; i < n; i++) { // 안내판의 숫자 n - 1번째까지 확인
		int plateOn = 0; // 번호판 불이 켜진 수
		int numOn = 0; // 숫자의 불이 켜진 수
		for (int j = 0; j < number[i].length(); j++) {
			if (number[i][j] == '#') {
				plateOn++;
				if (shape[x][j] == '#') {
					numOn++;
				}
			}
		}

		if (plateOn == numOn) { // 번호판과 숫자의 불이 켜진 갯수가 같으면 만들 수 있는 숫자
			num[i].push_back(x);
		}
	}
}


int main() {
	//초기화
	shape[0] = { "####.##.##.####" };
	shape[1] = { "..#..#..#..#..#" };
	shape[2] = { "###..#####..###" };
	shape[3] = { "###..####..####" };
	shape[4] = { "#.##.####..#..#" };
	shape[5] = { "####..###..####" };
	shape[6] = { "####..####.####" };
	shape[7] = { "###..#..#..#..#" };
	shape[8] = { "####.#####.####" };
	shape[9] = { "####.####..####" };

	cin >> n;
	for (int i = 0; i < 5; i++) {
		cin >> input[i];
	}

	//----------------------
	// 숫자 한줄(string)로 변형하기 / 숫자가 나올 수 없는 경우 판별
	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < n * 4 - 1; j++) {
			if (j % 4 == 3) { // 숫자와 숫자 사이 꺼진 전구는 넘어감
				continue;
			}

			if (j % 4 == 1 && (input[1][j] == '#' || input[3][j] == '#')) { //숫자가 나올 수 없는 경우
				cout << -1;
				return 0;
			}

			number[j / 4] += input[i][j]; //모양대로 입력한 숫자를 한줄로 바꿈
		}

	}
	//-----------------------
	// 번호판으로 가능한 숫자 판별
	for (int i = 0; i < 10; i++) { // 0 ~ 9 숫자 확인
		check(i);
	}

	//-----------------------
	// 평균 구하기
	int cnt = 0;
	while (cnt != n) {
		double sum = 0;
		for (int i = 0; i < num[cnt].size(); i++) {
			sum += num[cnt][i];
		}
		sum /= num[cnt].size();
		result = result + (sum * pow(10, abs(cnt - n) - 1));
		cnt++;
	}

	cout << result;

	return 0;
}
