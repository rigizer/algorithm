import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader rdin = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter rdout = new BufferedWriter(new OutputStreamWriter(System.out));
        int num = Integer.parseInt(rdin.readLine());

        for (int i = 0; i < num; i++) {
            StringTokenizer data = new StringTokenizer(rdin.readLine());
            int x1 = Integer.parseInt(data.nextToken());
            int y1 = Integer.parseInt(data.nextToken());
            int r1 = Integer.parseInt(data.nextToken());
            int x2 = Integer.parseInt(data.nextToken());
            int y2 = Integer.parseInt(data.nextToken());
            int r2 = Integer.parseInt(data.nextToken());

            double distToteam = Math.sqrt(Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2));
            int sumR = r1 + r2;
            int diffR = Math.abs(r1 - r2);

            if (distToteam == 0 && r1 == r2) {
                rdout.write("-1\n"); // 동일한 원 (무한대)
            } else if (distToteam > sumR || distToteam < diffR) {
                rdout.write("0\n"); // 외부에서 떨어진 경우 또는 내부에서 만나지 않는 경우
            } else if (distToteam == sumR || distToteam == diffR) {
                rdout.write("1\n"); // 외접 또는 내접
            } else {
                rdout.write("2\n"); // 두 점에서 만나는 경우
            }
        }
        
        rdout.flush();
        rdout.close();
    }
}