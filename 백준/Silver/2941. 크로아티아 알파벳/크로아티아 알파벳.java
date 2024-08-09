import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word = sc.next();
        
        word = word.replace("dz=", "D")
                   .replace("c=", "C")
                   .replace("c-", "C")
                   .replace("d-", "D")
                   .replace("lj", "L")
                   .replace("nj", "N")
                   .replace("s=", "S")
                   .replace("z=", "Z");
        
        System.out.println(word.length());
    }
}