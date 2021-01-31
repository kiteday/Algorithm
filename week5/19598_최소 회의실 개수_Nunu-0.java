import java.util.*;
//[19598] 최소 회의실 개수
//운영체제에서 배운 스케줄링이랑 비슷한 듯
public class Main {
	// pair을 사용하기 위한 클래스 <시간, >
	static class Pair implements Comparable<Pair>{
		int t, b; // t = 회의 시간, b = 시작인지 끝인지 구분

		public Pair(int t, int b) {
			this.t = t;
			this.b = b;
		}

		@Override
		public int compareTo(Pair c) {
			if(this.t == c.t)
				return this.b - c.b;
			else
				return this.t - c.t;
		}
	}

	// 메인 클래스
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n, cnt = 0, room = 0; // n = 회의 개수, cnt = 실시간 회의실 개수, room = 최대 회의실 개수
		int s, e; // s = 회의 시작 시간, e = 회의 끝나는 시간

		n = sc.nextInt(); // n = 회의 개수
		List<Pair> time = new ArrayList<>();
		// 회의 시간이 들어가는 리스트(페어) <시간, 시작 or 끝>

		for(int i = 0; i < n; i++) { // 회의 시간 입력 반복문
			s = sc.nextInt();
			e = sc.nextInt();
			time.add(new Pair(s, 1)); // 시작하는 시간 등록
			time.add(new Pair(e, -1));  // 끝나는 시간 등록
			// 시작하는 시간 = 1 끝나는 시간 = -1 로 구분
		}

		Collections.sort(time); // 회의가 시작하는 순서대로 정렬

		for (Pair a : time) { // 범위 기반 for문 time배열의 모든 요소를 방문
			cnt += a.b;
			// Pair<t, b> 중에 b를 가져와 회의가 시작하면 +1, 회의가 끝나면 +(-1)을 한다
			room = Math.max(cnt, room);
			// 실시간으로 회의실을 가장 많이 사용한 개수를 확인함
		}

		System.out.println(room);
	}
}
