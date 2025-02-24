import java.util.*;
import java.io.*;
//TIP 코드를 <b>실행</b>하려면 <shortcut actionId="Run"/>을(를) 누르거나
// 에디터 여백에 있는 <icon src="AllIcons.Actions.Execute"/> 아이콘을 클릭하세요.
public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int num = 0;
        while (true) {
            int n = Integer.parseInt(br.readLine());
            if (n == 0) {
                break;
            } else if (num != 0) {
                System.out.println();
            }

            Map<String, Integer> data = new HashMap<>();
            data.put("a", 1);

            for (int i = 0; i < n; i++) {
                String[] temp = new String[3];
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < 3; j++) {
                    temp[j] = st.nextToken();
                }

                String x = temp[0];
                String y = temp[2];

                if (data.containsKey(y)) {
                    data.put(x, data.get(y));
                } else if (data.containsKey(x) && !data.containsKey(y)) {
                    data.remove(x);
                }
            }

            num++;
            System.out.println("Program #" + num);

            if (data.isEmpty()) {
                System.out.println("none");
            } else {
                Set<String> result = data.keySet();
                result.stream().sorted().forEach(i -> System.out.print(i + " "));
                System.out.println();
            }
        }
    }
}