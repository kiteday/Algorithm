import java.util.Scanner;
//[1012] 유기농 배추
public class Main {
	static int t, m, n, k; // t = 테스트 개수, m = 가로, n = 세로, k = 배추 위치의 개수;
	static boolean[][] field; // 이차원 배열 배추밭
	static int[] loc = {1, -1, 0, 0};

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int x, y, cnt;
		t = sc.nextInt(); // 테스트 개수

		for(int i = 0; i < t; i++) { // 테스트
			m = sc.nextInt();
			n = sc.nextInt();
			k = sc.nextInt();

			field = new boolean[n][m];

			// 배추 심기
			for(int j = 0; j < k; j++) {
				y = sc.nextInt();
				x = sc.nextInt();
				field[x][y] = true;
			}

			cnt = 0; // 지렁이가 필요한 수

			// 배추흰지렁이 이동시키기
			for(int j = 0; j < n; j++) {
				for(int z = 0; z < m; z++) {
					if(field[j][z]) {
						cnt++;
						DS(j, z);
					}
				}
			}

			System.out.println(cnt);
		}
	}

	public static void DS(int y, int x) {
		int nx, ny;
		field[y][x] = false;

		for(int i = 0; i < 4; i++) {
			nx = x + loc[i];
			ny = y + loc[(i + 2) % 4];

			if (nx < 0 || ny < 0 || nx >= m || ny >= n) {
				continue;
			}
			if (field[ny][nx]) {
				DS(ny, nx);
			}
		}
	}
}
