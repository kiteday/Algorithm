import java.util.*;
//[11501] 주식
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt(); // t = 테스트 개수

		for(int i = 0; i < t; i++) {
			int n = sc.nextInt(); // n = 날의 수

			long max = 0, result = 0;
			// max = 주식이 가장 높은 가격, result = 최대 이익
			int price[] = new int[n]; // 주식 주가 배열

			// 주식 주가 입력
			for(int j = 0; j < n; j++) {
				price[j] = sc.nextInt();
			}

			// 뒤에서부터 검사
			for(int j = n - 1; j >= 0; j--) {
				if(price[j] > max) { // 현재보다 높은 주가가 있다면
					max = price[j]; // 높은 주가를 max에 대입
				}
				else { // 높은 주가가 없다면 (주가가 낮음)
					result += (max - price[j]); // 최대 주가(max)때 판매를 해 이익을 얻음
				}
			}

			System.out.println(result);
		}
	}
}
