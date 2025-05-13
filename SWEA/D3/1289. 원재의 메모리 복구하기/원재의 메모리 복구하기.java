import java.io.*;

public class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuffer sb = new StringBuffer();
        
        int tc = Integer.parseInt(br.readLine());
        for (int t = 1; t <= tc; t++) {
            String input = br.readLine();
            int s = input.length();
            boolean[] m = new boolean[s];
            for (int i = 0; i < s; i++) {
                m[i] = input.charAt(i) == '1';
            }

            boolean status = false;
            int result = 0;

            for (int i = 0; i < s; i++) {
                boolean tmp = m[i] ^ status;
                if (tmp) {
                    status = !status;
                }
                result += tmp ? 1 : 0;
            }

            sb.append("#").append(t).append(" ").append(result).append("\n");
            
        }
        bw.append(sb.toString());
        bw.flush();
    }
}