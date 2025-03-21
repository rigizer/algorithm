import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int[] count = new int[10_001];

        for (int i = 0; i < n; i++) {
            count[Integer.parseInt(br.readLine())]++;
        }

        for (int i = 0; i < 10_001; i++) {
            for (int j = 0; j < count[i]; j++) {
                wr.write(i + "\n");
            }
        }

        wr.flush();
        wr.close();
    }
}