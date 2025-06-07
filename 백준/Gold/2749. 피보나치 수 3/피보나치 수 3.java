import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int m = 1_000_000;
        int p = 15 * (m / 10);

        int[] arr = new int[p];
        long n = Long.parseLong(br.readLine());

        if (n == 0) {
            System.out.println(0);
        } else if (n == 1) {
            System.out.println(1);
        } else {
            arr[0] = 0;
            arr[1] = 1;
            for (int i = 2; i < p; i++) {
                arr[i] = (arr[i - 1] + arr[i - 2]) % m;
            }
            System.out.println(arr[(int)(n % p)]);
        }
    }
}