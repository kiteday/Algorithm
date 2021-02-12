import java.util.*;
import java.io.*;
// [2981] 검문
public class Main {
	static int n, gcd; // n = 숫자의 개수, gcd = 최대공약수
	static int[] m; // 숫자를 입력할 배열
	static List<Integer> p; // 소인수분해한 소수를 넣을 리스트

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		//위의 코드 2줄 [2617] 구슬 찾기에 설명 해둠

		n = Integer.parseInt(st.nextToken()); // 숫자의 개수
		m = new int[n]; // 숫자를 입력 할 배열
		p = new LinkedList<>(); // 소인수분해 소수 리스트

		for(int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());

			m[i] = Integer.parseInt(st.nextToken()); // 숫자 입력
		}

		Arrays.sort(m); // 작은수 ~ 큰수 정렬하기

		gcd = m[1] - m[0]; // 최소공약수를 가장 작은 수로 초기화

		// 인접한 숫자의 차들의 최대공약수를 구함
		for(int i = 2; i < n; i++) {
			gcd = GCD(gcd, m[i] - m[i - 1]);
		}

		// 소인수분해
		p.add(gcd);
		for(int i = 2; i * i <= gcd; i++) {
			if(gcd % i == 0) {
				p.add(gcd / i); // 중복 방지

				if((gcd / i) != i) {
					p.add(i);
				}
			}
		}

		Collections.sort(p); // 리스트 정렬

		for(int i = 0; i < p.size(); i++) {
			System.out.print(p.get(i) + " ");
		}

	}
	static int GCD(int a, int b) { // 유클리드 호제법으로 최대공약수 구하기
		int c;

		while (b != 0){
			c = a;
			a = b;
		    b = c % a;
		}

		return a;
	}
}
