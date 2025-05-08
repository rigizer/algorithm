import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        
        while (true) {
            int result = 0;
            st = new StringTokenizer(br.readLine());
            List<Integer> list = new ArrayList<>();
            while (st.hasMoreTokens()) {
                int n = Integer.parseInt(st.nextToken());
                if (n != 0) {
                    list.add(n);
                }
            }

            if (list.get(0) == -1) {
                break;
            }

            int size = list.size();
            for (int i = 0; i < size; i++) {
                for (int j = i + 1; j < size; j++) {
                    if (list.get(i) == list.get(j) * 2 || list.get(j) == list.get(i) * 2) {
                        result++;
                    }
                }
            }

            System.out.println(result);
        }
    }
}
