import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        while (true) {
            String line = br.readLine();
            if (line.equals("-1")) break;

            String[] tokens = line.split(" ");
            boolean[] exists = new boolean[101];
            int[] nums = new int[tokens.length];
            int size = 0;

            for (String token : tokens) {
                int n = Integer.parseInt(token);
                if (n == 0) break;
                nums[size++] = n;
                exists[n] = true;
            }

            int result = 0;
            for (int i = 0; i < size; i++) {
                int doubleVal = nums[i] * 2;
                if (doubleVal <= 100 && exists[doubleVal]) {
                    result++;
                }
            }

            sb.append(result).append("\n");
        }

        System.out.print(sb);
    }
}
