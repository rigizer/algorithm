import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Long n = Long.parseLong(br.readLine());
        int result = 0;

        while (n > 1) {
            if (n % 2 == 0) n /= 2;
            else n++;
            result++;
        }

        System.out.println(result);
    }
}