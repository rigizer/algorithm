import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Long n = Long.parseLong(br.readLine());
        int result = 0;

        while (true) {
            if (n == 1) break;
            result++;

            if (n % 2 == 0) n /= 2;
            else n++;
        }

        System.out.println(result);
    }
}