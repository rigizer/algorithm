import java.io.*;
import java.util.*;

class Solution {
    private static int calc(int n, int m, int[] a, int[] b) {
        int result = 0;
        
        for (int i = 0; i < m - n + 1; i++) {
            int sum = 0;
            for (int j = 0; j < n; j++) {
                sum += a[j] * b[i+ j];
            }
            
            result = Math.max(result, sum);
        }
        
        return result;
    }
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        
        int t = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= t; tc++) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            int[] a = new int[n];
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                a[i] = Integer.parseInt(st.nextToken());
            }
            int[] b = new int[m];
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < m; i++) {
                b[i] = Integer.parseInt(st.nextToken());
            }
            int result = n <= m ? calc(n, m, a, b) : calc(m, n, b, a);
            System.out.println("#" + tc + " " + result);
        }
    }
}