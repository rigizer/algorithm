import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Map<String, Integer> countMap = new HashMap<>();

        while (true) {
            String ssn = br.readLine();
            if (ssn.equals("000-00-0000")) {
                break;
            }

            countMap.put(ssn, countMap.getOrDefault(ssn, 0) + 1);
        }

        List<String> duplicates = new ArrayList<>();

        for (Map.Entry<String, Integer> entry : countMap.entrySet()) {
            if (entry.getValue() > 1) {
                duplicates.add(entry.getKey());
            }
        }

        Collections.sort(duplicates);

        StringBuilder sb = new StringBuilder();
        for (String ssn : duplicates) {
            sb.append(ssn).append('\n');
        }

        System.out.print(sb.toString());
    }
}