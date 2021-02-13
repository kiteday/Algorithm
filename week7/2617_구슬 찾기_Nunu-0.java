import java.util.*;
import java.io.*;
//[2617] 구슬 찾기
public class Main {

	static int n, m; // n = 구슬 개수, m = 저울에 올려 본 쌍의 개수
	static List<Integer>[] h; // 쌍중에 무거운 구슬을 넣을 리스트
	static List<Integer>[] l; // 쌍중에 가벼운 구슬을 넣을 리스트
	static boolean[] visit; // 방문한 구슬인지 확인
	static int cnt; // 무겁거나 가벼운 구슬의 개수

	public static void main(String[] arge) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		// BufferReader가 Scanner보다 속도가 빠르다
		// 둘다 문자열을 입력 받는데 사용
		// BufferReader은 String형태로 입력을 받음 (정수형은 Integer.parseInt() 사용)
		StringTokenizer st = new StringTokenizer(br.readLine());
		// 공백을 기준으로 입력 받아야 할때 사용

		n = Integer.parseInt(st.nextToken()); // n = 구슬 개수
		m = Integer.parseInt(st.nextToken()); // m = 쌍의 개수
		h = new ArrayList[n + 1]; // 쌍에서 무거울 구슬을 넣을 배열 리스트(구슬의 개수 만큼)
		l = new ArrayList[n + 1]; // 쌍에서 가벼운 구슬을 넣을 배열 리스트(구슬의 개수 만큼)
		visit = new boolean[n + 1]; // 방문한 구슬인지 확인하는 배열

		int result = 0; // 가운데 구슬 (결과)

		// 구슬의 개수 만큼 배열리스트를 만든다
		for(int i = 1; i <= n; i++) {
			h[i] = new ArrayList<>();
			l[i] = new ArrayList<>();
		}

		// 구슬 쌍 입력
		for(int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine()); // 위에도 썼는데 두 번 안쓰면 왠지 오류남

			int a = Integer.parseInt(st.nextToken()); // 무거운 구슬
			int b = Integer.parseInt(st.nextToken()); // 가벼운 구슬
			h[b].add(a); // b구슬 보다 무거운 a구슬을 b구슬 리스트에 넣는다
			l[a].add(b); // a구슬 보다 가벼운 b구슬을 a구슬 리스트에 넣는다
		}

		// 가운데 구슬 찾기
		for(int i = 1; i <= n; i++) {
			// (n - 1) / 2 이상의 구슬이 무겁거나 가벼우면 그 구슬은 중간에 올 수 없음

			// 무거운 구슬 개수 구하기
			Arrays.fill(visit, false); // visit 배열을 false로 초기화
			cnt = 0; // dfs를 통해 구하는 무겁거나 구슬의 개수
			dfs(i, h);
			if (cnt >= (n + 1) / 2) {
				result++;
				continue; // 가벼울때는 넘겨서 시간 단축
			}

			// 가벼운 구슬 개수 구하기
			Arrays.fill(visit, false); // visit 배열을 false로 초기화
			cnt = 0; // dfs통해 구하는 가벼운 구슬의 개수
			dfs(i, l);
			if(cnt >= (n + 1) / 2) {
				result++;
			}
		}

		System.out.println(result);
		br.close();
	}

	static void dfs(int bead, List<Integer>[] AL) {
		visit[bead] = true;

		for(int i = 0; i < AL[bead].size(); i++) {
			if(!visit[AL[bead].get(i)]) { // 방문하지 않은 구슬이라면
				cnt++;
				dfs(AL[bead].get(i), AL);
			}
		}
	}
}
