import java.io.*;

public class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        
        int tc = Integer.parseInt(br.readLine());
        for (int t = 1; t <= tc; t++) {
            String input = br.readLine();
            int s = input.length();
            boolean status = false;
            int result = 0;
            for (int i = 0; i < s; i++) {
                if ((input.charAt(i) == '1') != status) {
                    status = !status;
                    result++;
                }
            }
            sb.append('#').append(t).append(' ').append(result).append('\n');
        }
        System.out.println(sb);
    }
}