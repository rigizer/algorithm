import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), "-");

        List<String> exp = new ArrayList<>();
        while (st.hasMoreTokens()) {
            exp.add(st.nextToken());
        }
        int result = 0;
        
        List<Integer> num = new ArrayList<>();
        for (String i: exp) {
            int sum = 0;
            st = new StringTokenizer(i, "+");
            List<String> subExp = new ArrayList<>();
            while (st.hasMoreTokens()) {
                subExp.add(st.nextToken());
            }
            for (String j: subExp) {
                sum += Integer.parseInt(j);
            }
            num.add(sum);
        }

        result = num.get(0);
        for (int i = 1; i < num.size(); i++) {
            result -= num.get(i);
        }

        System.out.println(result);
    }
}