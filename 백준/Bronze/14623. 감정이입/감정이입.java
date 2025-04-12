import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        long b1 = Long.parseLong(br.readLine(), 2);
        long b2 = Long.parseLong(br.readLine(), 2);

        System.out.println(Long.toBinaryString(b1 * b2));
    }
}