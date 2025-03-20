import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws Exception {
		 BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		 StringTokenizer st = new StringTokenizer(br.readLine());
		 int n = Integer.parseInt(st.nextToken());
		 StringBuilder sb = new StringBuilder();
		 sb.append(st.nextToken());
		 System.out.println(sb.charAt(sb.length() - 1));
	}
}