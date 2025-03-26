import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader I = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter O = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(I.readLine());

        String t = "BCMW";
        while (n-- > 0) {
            int[] d = new int[4];
            StringTokenizer s = new StringTokenizer(I.readLine());
            String a = s.nextToken(), b = s.nextToken();
            StringBuilder as = new StringBuilder(a);

            for (int i = 0; i < b.length(); i++) {
                d[t.indexOf(b.charAt(i))]++;
            }

            d[0] *= 2; 
            d[2] *= 4; 
            d[3] *= 3;

            int max = Arrays.stream(d).max().getAsInt();
            int count = 0, index = -1;
            for (int i = 0; i < 4; i++) {
                if (d[i] == max) {
                    count++;
                    index = i;
                }
            }

            if (count > 1) {
                as.append(": There is no dominant species");
            } else {
                String[] species = {"Bobcat", "Coyote", "Mountain Lion", "Wolf"};
                as.append(": The ").append(species[index]).append(" is the dominant species");
            }

            O.write(as + "\n");
        }
        O.flush();
    }
}