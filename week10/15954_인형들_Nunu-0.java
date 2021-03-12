import java.util.*;
import java.io.*;
// [15954] 인형들
public class Main {
	public static int n, k;
	public static int[] pre; //preferences
	public static double m, v; // 평균, 분산
	public static double min = 10000000; // 최소 표준편차

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		n = Integer.parseInt(st.nextToken()); // 인형의 종류 개수 입력
		k = Integer.parseInt(st.nextToken()); // 연속하는 인행의 수 입력
		pre = new int[n]; // 각 인형의 선호도

		st = new StringTokenizer(br.readLine());
		for(int i = 0; i < n ; i++) {
			pre[i] = Integer.parseInt(st.nextToken()); // 인형의 선호도 입력
		}

		for(int i = 0; i <= n - k; i++) { // 인형의 연속이 시작되는 위치
			for(int j = i + k - 1; j < n; j++) { // 연속의 끝이 되는 위치
				m = 0;

				for(int k = i; k <= j; k++) { // i부터 j까지의 총합
					m += pre[k];
				}

				m /= (j - i + 1); // 평균 구하기

				v = 0;
				for(int k = i; k <= j; k++) { // 분산 구하는 합
					v += Math.pow(pre[k] - m, 2);
				}
				v /= (j - i + 1); // 분산 구하기

				min = Math.min(min, Math.sqrt(v)); // 최소의 표준 편차 구하기
			}
		}

		System.out.println(String.format("%.11f", min));
	}
}
