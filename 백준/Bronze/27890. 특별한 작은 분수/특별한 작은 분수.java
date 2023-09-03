import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int x0 = Integer.parseInt(st.nextToken());
		int n = Integer.parseInt(st.nextToken());
		
		for (int i = 0; i < n; i++) {
			if (x0 % 2 == 0) {
				x0 = ((x0 / 2) ^ 6);
			} else {
				x0 = ((2 * x0) ^ 6);
			}
		}
		
		System.out.println(x0);
	}
}