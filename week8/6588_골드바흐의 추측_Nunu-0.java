import java.util.*;
import java.io.*;
// [6588] 골드바흐의 추측
public class Main {
	public static int n; // n = 정수
	public static boolean[] PN = new boolean[1000001]; // 소수를 확인할 배열
	// prime number = 소수면 false 아니면 true

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		primeN(); // 소수 찾기

		while(true) {
			n = Integer.parseInt(br.readLine()); // 정수 입력

			if(n == 0) { // 0이 입력되면 멈춘다
				break;
			}

			PN[0] = false; // 사용하지않는 PN[0]을 이용해 두 홀수소수를 찾았는지 확인

			// n = a + b 가 성립하는 b = 큰 소수, a = 작은 소수 구하기
			for(int a = 3; a <= n / 2; a++) { // a < b 이기 때문에 n / 2를 넘으면 x
				if(!PN[a]) { //
					if(!PN[n - a]) { // n - a = b가 소수인지 확인
						System.out.println(n + " = " + a + " + " + (n - a));
						PN[0] = true;
						break;
					}
					// n - b 가 소수가 아니면 다음으로 큰 소수를 찾는다
				}
			}

			if(!PN[0]) { // 두 홀수소수를 찾지 못했다면
				System.out.println("Goldbach's conjecture is wrong.");
			}
		}
	}

	// 소수 찾기 (에라토스테네스의 체 사용)
	// 자신을 제외한 배수를 삭제함
	static void primeN(){
		for(int i = 2; i < 1000001; i++) {
			if(!PN[i]) { // 소수 = false
				// i(소수)의 배수를 전부 false로 바꿈
				for(int j = i * 2; j < 1000001; j += i) {
					PN[j] = true; // 소수가 아닌숫자 = true
				}
			}
		}
	}
}
