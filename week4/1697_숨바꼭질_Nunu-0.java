import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
//[1697] 숨바꼭질
/*
수빈이가 이동할 수 있는 방법
1. n + 1
2. n - 1
3. n * 2

이동할 수 있는 모든 경우를 queue에 넣고
가장 빨리 동생의 위치를 찾은 시간을 구한다.
*/
public class Main {
	static int n, k;
	static int[] time = new int[100001]; // 몇초 걸렸는지 체크

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt(); // 수빈이의 위치
		k = sc.nextInt(); // 동생의 위치

		bfs(n, k);
	}

	static void bfs(int n, int k) {
		Queue<Integer> q = new LinkedList<>(); // 큐

		q.add(n); // 수빈이의 처음 위치 push
		time[n] = 1;

		while(!q.isEmpty()) {
			int loc = q.poll(); // 현재 위치, 맨 앞 데이터 추출 후 pop

			if(loc == k) { // 동생을 찾으면 while 탈출
				break;
			}

			if (loc + 1 <= 100000 && time[loc + 1] == 0) { // n + 1로 이동하고 시간은 1초 늘어남
				q.add(loc + 1);
				time[loc + 1] = time[loc] + 1;
			}
			if (loc - 1 >= 0 && time[loc - 1] == 0) { // n - 1로 이동하고 시간은 1초 늘어남
				q.add(loc - 1);
				time[loc - 1] = time[loc] + 1;
			}
			if (loc * 2 <= 100000 && time[loc * 2] == 0) { // n * 2로 이동하고 시간은 1초 늘어남
				q.add(loc * 2);
				time[loc * 2] = time[loc] + 1;
			}
		}
		System.out.println(time[k] - 1);
	}
}
