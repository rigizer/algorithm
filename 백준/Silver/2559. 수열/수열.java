import java.io.*;
import java.util.*;
class Main{
    public static void main(String[] args)throws Exception{
        BufferedReader I=new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st=new StringTokenizer(I.readLine());
        int n=Integer.parseInt(st.nextToken()),k=Integer.parseInt(st.nextToken());

        int[] num=new int[n+1];
        st=new StringTokenizer(I.readLine());
        for(int i=1;i<=n;i++){
            num[i]=num[i-1]+Integer.parseInt(st.nextToken());
        }
        int max=Integer.MIN_VALUE,l=n-k;
        for(int i=0;i<=l;i++){
            max=Math.max(max,num[i+k]-num[i]);
        }
        System.out.println(max);
    }
}