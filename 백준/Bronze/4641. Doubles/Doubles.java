import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        while (true) {
            st = new StringTokenizer(br.readLine());
            List<Integer> list = new ArrayList<>();
            Set<Integer> set = new HashSet<>();

            while (st.hasMoreTokens()) {
                int n = Integer.parseInt(st.nextToken());
                if (n == 0) break;
                list.add(n);
                set.add(n);
            }

            if (list.size() == 1 && list.get(0) == -1) break;

            int result = 0;
            for (int num : list) {
                if (set.contains(num * 2)) {
                    result++;
                }
            }

            System.out.println(result);
        }
    }
}
