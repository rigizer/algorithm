import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String isbn = br.readLine();
        int result = 0;
        boolean isEven = false;

        for (int i = 0; i < 13; i++) {
            char ch = isbn.charAt(i);
            if (ch == '*') {
                if (i % 2 != 0) {
                    isEven = true;
                }
                continue;
            }
            int num = ch - '0';
            result += num * (i % 2 == 0 ? 1 : 3);
        }

        if (isEven) {
            for (int i = 0; i < 10; i++) {
                if ((result + (i * 3)) % 10 == 0) {
                    System.out.println(i);
                    break;
                }
            }
        } else {
            System.out.println((10 - result % 10) % 10);
        }
    }
}
