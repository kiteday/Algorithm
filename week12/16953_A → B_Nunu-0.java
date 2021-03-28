import java.util.*;
import java.io.*;
// [16953] A → B
public class Main {
	public static long a, b;
	public static int min = 100000, cnt;

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st= new StringTokenizer(br.readLine());

		a = Integer.parseInt(st.nextToken()); // a 입력
		b = Integer.parseInt(st.nextToken()); // b 입력

		bfs(a, 1);

		if(min == 100000) // a가 b를 만들 수 없는 경우
			System.out.println("-1");
		else
			System.out.println(min);
	}

	static void bfs(long a, int cnt) {
		if (a > b) // 계산한 a 값이 b를 넘을 수 없다
			return;

		if (a == b) // a와 b가 같아졌을 때 최소연산횟수를 구한다
			min = Math.min(min, cnt);

		bfs(a * 2, cnt + 1); // 2를 곱한다
		bfs(a * 10 + 1, cnt + 1); // 1을 수의 가장 오른쪽에 추가한다
		// ++cnt로 했었는데 예제 2 162 를 입력하면 6이 나왔다..이유를 모르겠음
	}
}
