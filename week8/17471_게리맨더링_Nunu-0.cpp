#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;
// [17471] 게리맨더링
int n; // 구역의 개수
int person[11]; // 각 구역의 인물 수
bool link[11][11]; // 지역이 연결 됐는지 확인 배열
bool visit[11]; // 방문한 구역 확인
bool team[11]; // a구역(false)인지 b구역(true)인지 구분
queue<int> q;
int rst = 10000;

int bfs(int area) {
	int cnt = 1;
	visit[area] = true;
	q.push(area);

	while(!q.empty()){
		int temp = q.front();
		q.pop();

		for(int i = 1; i <= n; i++){
			if (link[temp][i] && !visit[i] && team[temp] == team[i]) {
				visit[i] = true;
				q.push(i);
				cnt++;
			}
		}
	}
	return cnt;
}

void check(int area) {
	// 구역이 전부 분할 됐으면
	if (area > n) {
		int a = 0, b = 0; // a, b 구역 (2개의 구역)
		fill_n(visit, sizeof(visit), false); // 방문 구역 false 초기화

		a = bfs(1); // bfs()로 a구역의 개수 확인
		if (a == n) { // a == n 이면 b구간이 없으므로 있을 수 x
			return;
		}

		// a, b 구역 분할
		for (int i = 2; i <= n; i++) {
			if (!visit[i]) { // a 구역이 아닌 구역 찾기
				b = bfs(i); // b구역의 개수 구하기
				break;
			}
		}

		if (a + b != n) { // a + b = n 이 아니면 구역이 2개 이상인 것
			return;
		}

		// a와 b에 인물 수를 넣기위해 0으로 초기화
		a = 0;
		b = 0;

		// 각 구역 간 인구 수 구하기
		for (int i = 1; i <= n; i++) {
			if (team[i]) {
				a += person[i];
			}
			else {
				b += person[i];
			}
		}

		// 각 구역 간 인구 수의 최소 차 구하기
		int sum = a > b ? a - b : b - a;
		rst = min(rst, sum);
		return;
	}

	// 2개의 구역으로 모두 탐방함
	team[area] = false;
	check(area + 1);
	team[area] = true;
	check(area + 1);
}

int main(){

	cin >> n;

	// 인물 수 입력하기
	for (int i = 1; i <= n; i++) {
		cin >> person[i];
	}

	// 각 구역마다 인접한 구역 입력
	for (int i = 1; i <= n; i++) {
		int a; // 인접한 구역의 개수
		cin >> a;

		for (int j = 0; j < a; j++) {
			int b; // 인접한 구역 숫자
			cin >> b;

			link[i][b] = true;
		}
	}

	fill_n(team, sizeof(team), false); // false 초기화

	check(1);

	if (rst == 10000) {
		cout << -1;
	}
	else {
		cout << rst;
	}

	return 0;
}
