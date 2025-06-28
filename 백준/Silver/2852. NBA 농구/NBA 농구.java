import java.io.*;
import java.util.*;

public class Main {
    public static int ascore = 0;
    public static int bscore = 0;
    public static int atime = 0;
    public static int btime = 0;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        
        int n = Integer.parseInt(br.readLine());
        int lastIdx = 0;
        int[][] data = new int[n][2];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            data[i][0] = Integer.parseInt(st.nextToken());
            data[i][1] = stringToTime(st.nextToken());
        }

        for (int i = 0; i < 2880; i++) {
            if (lastIdx < n && data[lastIdx][1] == i) {
                if (data[lastIdx][0] == 1) ascore++;
                else bscore++;
                lastIdx++;
            }

            if (ascore > bscore) atime++;
            else if (ascore < bscore) btime++;
        }

        System.out.println(timeToString(atime));
        System.out.println(timeToString(btime));
    }

    private static int stringToTime(String time) {
        String[] t = time.split(":");
        return Integer.parseInt(t[0]) * 60 + Integer.parseInt(t[1]);
    }

    private static String timeToString(int time) {
        return (time / 60 < 10 ? "0" : "") + time / 60 + ":" + (time % 60 < 10 ? "0" : "") + time % 60;
    }
}