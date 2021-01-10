#include <iostream>
#include <queue>
using namespace std;
// [7576] 토마토
/*
	BFS를 사용
	1. queue안에 익은 토마토를 넣는다
	2. queue안의 첫번째 토마토를 pop하고 그 토마토의 상하좌우를 queue안에 넣는다.
	3. queue가 비어질 때까지 2를 반복한다. (익힐 수 있는 모든 토마토를 익힌다)
*/
int m, n, day = 0; // 상자의 m = 가로, n = 세로, day = 걸린 날짜
int box[1001][1001];
int loc[4] = { 1, -1, 0, 0 }; // 상하좌우
queue<pair<int, int>> q;

void BFS() {
	int x, y, x1, y1;
	while (q.size() != 0) { // queue가 비어있는지 (비어있으면 true, 있으면 false)
		x = q.front().first; // q의 왼쪽
		y = q.front().second; // q의 오른쪽
		q.pop();

		for (int i = 0; i < 4; i++){ // pop한 토마토의 상하좌우를 익히고 queue안에 넣는다.
			x1 = x + loc[i];
			y1 = y + loc[(i + 2) % 4];

			if ((x1 < 0 || x1 >= n || y1 < 0 || y1 >= m)) {
				continue;
			}
			if (box[x1][y1] == 0 ) { // 익지않은 토마토를 익힘
				box[x1][y1] = box[x][y] + 1; // box안에 몇일차에 익었는지 넣음
				q.push({x1, y1});
			}
		}
	}
}

int main() {

	cin >> m >> n;

	for (int i = 0; i < n; i++) { // 토마토의 상태
		for (int j = 0; j < m; j++) {
			cin >> box[i][j];
			if (box[i][j] == 1) { // 토마토가 익었다면 queue에 넣기
				q.push({i, j});
			}
		}
	}

	BFS(); // BFS로 토마토 익히기

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (box[i][j] == 0) { // 익지않은 토마토가 존재하면 -1을 출력
				cout << "-1";
				return 0;
			}
			if (day < box[i][j]) { // 박스안에 등록했던 가장 높은 날짜를 day에 넣기
				day = box[i][j];
			}
		}
	}
	cout << day - 1;
}
