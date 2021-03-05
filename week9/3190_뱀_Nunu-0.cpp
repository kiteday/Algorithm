#include <iostream>
#include <queue>
#include <vector>
using namespace std;
// [3190] 뱀
int n, k, l, x; // n = 보드의 크기, k = 사과 개수, l = 방향 변환 횟수, x = 초
char c; // 뱀의 방향
int a, b, time; // a, b = 사과의 위치 좌표

int map[101][101] = {}; // 비어있으면 = 0, 사과의 위치 = 1, 뱀의 위치 = 2
queue <pair<int, int>> snake; // 뱀의 위치
vector <pair<int, char>> snakeL; // 뱀의 방향 정보
int hx, hy, tx, ty; // 뱀 머리, 꼬리의 x, y좌표
int Loc[4] = {0, 0, 1, -1};  // 상하좌우
int L[4] = { 3, 2, 0, 1 }; // 회전 왼쪽
int R[4] = { 2, 3, 1, 0 }; // 회전 오른쪽
int cnt, d; // 몇번째 방향정보인지, d = 방향이 어딘지

// 게임 시작(뱀 움직이기)
void play() {
	//뱀 시작자리 초기화
	snake.push(make_pair(0, 0));
	map[hx][hy] = 2;

	while (1) {
		time++;
		hx += Loc[d];
		hy += Loc[(d + 2) % 4];

		// 벽 또는 뱀의 몸과 부딪히면 게임 끝
		if (hx < 0 || hx >= n || hy < 0 || hy >= n || map[hx][hy] == 2) {
			break;
		}

		// 이동할 때 사과가 없으면 꼬리지우기
		if (map[hx][hy] == 0) {
			tx = snake.front().first;
			ty = snake.front().second;
			snake.pop();
			map[tx][ty] = 0;
		}
		map[hx][hy] = 2; // 뱀머리 이동
		snake.push({ hx, hy });

		if(cnt < l){
			if (time == snakeL[cnt].first) { // 회전 할 시간이면
				if (snakeL[cnt].second == 'L') { // 왼쪽으로 돈다면
					d = L[d];
				}
				else { // 오른쪽으로 돈다면
					d = R[d];
				}
				cnt++;
			}
		}
	}
}

int main() {
	cin >> n >> k;

	// 사과 좌표 입력
	for (int i = 0; i < k; i++) {
		cin >> a >> b;
		map[a - 1][b - 1] = 1;
	}

	// 뱀의 뱡향 정보 입력
	cin >> l;
	for (int i = 0; i < l; i++) {
		cin >> x >> c;
		snakeL.push_back({ x, c });
	}

	//게임 시작
	play();

	cout << time;

	return 0;
}
