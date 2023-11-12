import java.util.Scanner;

class Solution {
   static int score = 0;
   static int N;
   static int L;
   static int[] tasty;
   static int[] cal;

   public static void main(String args[]) throws Exception {
      Scanner sc = new Scanner(System.in);
      int T;
      T = sc.nextInt();

      for (int test_case = 1; test_case <= T; test_case++) {
         N = sc.nextInt();
         L = sc.nextInt();

         tasty = new int[N];
         cal = new int[N];

         for (int i = 0; i < N; i++) {
            tasty[i] = sc.nextInt();
            cal[i] = sc.nextInt();
         }

         score = 0; // 각 테스트 케이스마다 초기화
         dfs(0, 0, 0);

         System.out.println("#" + test_case + " " + score);
      }
   }

   public static void dfs(int idx, int sumT, int sumC) {
      if (idx == N) {
         if (sumC <= L) {
            score = Math.max(score, sumT);
         }
         return;
      }
      dfs(idx + 1, sumT + tasty[idx], sumC + cal[idx]); // 맛과 칼로리 누적
      dfs(idx + 1, sumT, sumC); // 누적되지 않은 경우
   }
}