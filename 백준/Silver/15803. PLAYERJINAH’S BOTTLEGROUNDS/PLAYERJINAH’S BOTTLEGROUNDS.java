import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input1 = br.readLine().split(" ");
        String[] input2 = br.readLine().split(" ");
        String[] input3 = br.readLine().split(" ");

        int x1 = Integer.parseInt(input1[0]);
        int y1 = Integer.parseInt(input1[1]);

        int x2 = Integer.parseInt(input2[0]);
        int y2 = Integer.parseInt(input2[1]);

        int x3 = Integer.parseInt(input3[0]);
        int y3 = Integer.parseInt(input3[1]);

        int crossProduct = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1);
        System.out.println(crossProduct == 0 ? "WHERE IS MY CHICKEN?" : "WINNER WINNER CHICKEN DINNER!");
    }
}
