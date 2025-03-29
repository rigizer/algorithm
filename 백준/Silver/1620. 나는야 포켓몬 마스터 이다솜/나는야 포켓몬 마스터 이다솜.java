import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringBuffer sb = new StringBuffer();
        StringTokenizer st = new StringTokenizer(br.readLine());

        Map<String, String> map = new HashMap<>();

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        for (int i = 1; i <= n; i++) {
            String a = String.valueOf(i);
            String b = br.readLine();
            
            map.put(a, b);
            map.put(b, a);
        }

        for (int i = 0; i < m; i++) {
            String key = br.readLine();
            String value = map.get(key);

            sb.append(value + "\n");
        }
        sb.append("\n");

        bw.write(sb.toString());
        bw.close();
    }
}
