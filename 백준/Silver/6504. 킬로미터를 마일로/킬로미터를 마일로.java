import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());

        ArrayList<Integer> fib = new ArrayList<>();
        fib.add(1);
        fib.add(2);

        while (fib.get(fib.size() - 1) <= 25000) {
            int size = fib.size();
            fib.add(fib.get(size - 1) + fib.get(size - 2));
        }

        StringBuilder sb = new StringBuilder();

        while (t-- > 0) {
            int x = Integer.parseInt(br.readLine());
            int y = 0;

            for (int i = fib.size() - 1; i >= 0; i--) {
                if (fib.get(i) <= x) {
                    x -= fib.get(i);

                    if (i - 1 >= 0) {
                        y += fib.get(i - 1);
                    }

                    i--;
                }
            }

            sb.append(y).append('\n');
        }

        System.out.print(sb.toString());
    }
}