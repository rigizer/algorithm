import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int minA = 99999;
		int minB = 99999;
		
		for(int i = 0; i < n; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			if(minB > b) {
				minB = b;
				minA = a;
			}
		}
        
		System.out.println(minA + " " + minB);
		sc.close();
	}
}