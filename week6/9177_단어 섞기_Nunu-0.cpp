#include <iostream>
#include <string>
#include <vector>
using namespace std;
// [9177] 단어 섞기

string fr, sc, td; // fr = 첫번째 단어, sc = 두번째, td = 세번째
bool complete; // 단어를 완성했는지 확인

bool check() { // 단어를 만들 수 있는지 체크하는 함수
	if (fr.size() + sc.size() != td.size()) { // 첫번째,두번째 단어의 합이 세번째 단어의 길이다
		return false; // complete = flase
	}

	// 첫번째 길이 + 두번째 길이 = 세번째 길이가 증명된후 다른 알파벳이 들어왔는지 확인
	vector <int> alp(27, 0); // alp[27] = {}
	for (int i = 0; i < fr.size(); i++) { // 첫번째 단어 알파벳 추가
		alp[fr[i] - 'a']++;
	}
	for (int i = 0; i < sc.size(); i++) { // 두번째 단어 알파벳 추가
		alp[sc[i] - 'a']++;
	}
	for (int i = 0; i < td.size(); i++) { // 세번째 단어 알파벳 빼기
		alp[td[i] - 'a']--;
	}

	for (int i = 0; i < 26; i++) { // alp[]안에 0이 아니라면 다른 알파벳이 있다는 의미
		if (alp[i] != 0)
			return false;
	}

	return true;
}

void bfs(int fP, int sP, int tP) { // 각 fr, sc, td 단어의 알파벳 위치
	if (complete) { // 이미 단어가 만들어지면 탈출
		return;
	}

	if (td.size() == tP) { // 세번째 단어를 다만들면 dfs 탈출
		complete = true;
		return;
	}

	if (fr[fP] == td[tP]) { // 첫번째 단어의 알파벳을 사용한다면
		bfs(fP + 1, sP, tP + 1);
	}
	if (sc[sP] == td[tP]) { // 두번째 단어의 알파벳을 사용한다면
		bfs(fP, sP + 1, tP + 1);
	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL); // 시간 단축

	int t;
	cin >> t;

	for (int i = 1; i <= t; i++) {
		complete = false;
		cin >> fr >> sc >> td;

		if (check()) { // 세번째 문자을 만들 수 있는지 확인
			bfs(0, 0, 0);
		}

		if (complete) {
			cout << "Data set " << i << ": " << "yes" << endl;
		}
		else {
			cout << "Data set " << i << ": " << "no" << endl;
		}
	}

	return 0;
}
