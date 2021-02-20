import java.util.*;
import java.io.*;
// [2011] 암호코드
public class Main { // 클래스이름 Main으로 안하면 백준에서 컴파일 에러 남!
	public static String num;
	public static int []dp;
	public static int m = 1000000;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		num = new String(br.readLine()); // 숫자 입력
		dp = new int[num.length() + 1]; // dp의 길이 = 숫자의 길이 + 1
		Arrays.fill(dp, 0); // dp배열 0으로 초기화

		if (num.charAt(0) == '0') { // 입력된 숫자가 0인가
			dp[0] = 0; // dp[0] = 0이면 DP 시작이 안됨
		}
		else {
			dp[0] = 1;
		}

		for(int i = 1; i <= num.length(); i++) {

			// 0 일때 나올 수 있는 알파벳 x
			if(num.charAt(i - 1) != '0') {
				dp[i] += (dp[i - 1] % m);
			}
			// 2의 자리 숫자일 때
			if(i > 1) {
				int n = (num.charAt(i - 2) - '0') * 10 + (num.charAt(i - 1) - '0'); // 2자리수의 숫자 구하기
				if(n > 9 && n < 27) { // 2의 자리수일 때 알파벳을 만들 수 있으며
					dp[i] += (dp[i - 2] % m);
				}
			}
		}

		System.out.println(dp[num.length()] % m);
	}

}
