import java.util.*;
// [1756] 피자 굽기
public class Main {
	public static void main(String[] arge) {
		Scanner sc = new Scanner(System.in);

		int d = sc.nextInt(); // d = 오븐 깊이
		int n = sc.nextInt(); // n = 반죽 개수
		int oven[] = new int[d]; // oven = 상당부터 오븐의 지름
		int pizza[] = new int[n]; // pizza = 완성 된 순서의 피자 지름

		// 오븐 지름 입력
		for(int i = 0; i < d; i++) {
			oven[i] = sc.nextInt();

			// 입력된 오븐지름이 위의 오븐 크기보다 크면 위의 오븐 지름과 같은 크기로 만들어 줌
			// 아래서 위로 갈수록 넓어지는 오븐의 형태 (∨)
			if (i != 0 && oven[i] > oven[i - 1]) {
				oven[i] = oven[i - 1];
			}
		}

		// 피자 지름 입력
		for(int i = 0; i < n; i++) {
			pizza[i] = sc.nextInt();
		}

		int depth = d - 1; // 피자가 들어갈 수 있는 깊이
		int oinp = 0; // 오븐 안에 피자가 들어간 개수

		// 완성된 순서대로 피자 오븐에 넣기
		// 오븐의 아래부터 검사함
		while(depth >= 0) {
			if (oven[depth] >= pizza[oinp]) { // 들어갈 수 있는 제일 하단에 피자가 들어감
				oinp++;
			}

			if(oinp == n) { // 반죽한 피자가 전부 들어갔으면
				System.out.println(depth + 1);
				return;
			}
			depth--;
		}

		// 피자가 덜 들어갔으면
		System.out.println("0");
	}
}
