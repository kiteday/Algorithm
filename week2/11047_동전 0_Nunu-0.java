import java.util.Scanner; // Scanner 클래스 파일 가져오기 (사용자 입력)
//[11047] 동전 0
public class main { // 백준에서 클래스명을 Main로 해야함
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in); // Sacanner 변수를 sc로 설정해 기능 사용
		/*
		 * new : 메모리 공간을 선언
		 * Scanner(System.in) : 입력받은 데이터를 자바안으로 가져옴
		 */

		int n = sc.nextInt(); // 동전 입력
		int k = sc.nextInt(); // 가치 입력
		int[] value = new int[n]; // 각 동전의 가치
		int rst = 0; // 필요한 동전의 개수

		for(int i = 0; i < n; i++) {
			value[i] = sc.nextInt();
		}

		for(int i = n - 1; i >= 0; i--) { // 모든 동전을 확인하면 빠져 나옴
			if (value[i] <= k) { // 가치(k)와 가장 가깝고 낮은 동전의 가치 찾기
				rst += k / value[i];  // 가치 ÷ 가장 가치가 높은 필요한 동전
				k %= value[i];
			}
		}
		System.out.println(rst);
	}

}
