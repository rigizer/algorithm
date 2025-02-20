import java.io.*;
import java.util.*;

public class Main {
    static boolean[][] map;
    static List<Node> nodeList;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int TC = Integer.parseInt(br.readLine());

        while (TC-- > 0) {
            nodeList = new ArrayList<>();
            int martCnt = Integer.parseInt(br.readLine());
            int size = martCnt + 2;
            map = new boolean[size][size];

            for (int i = 0; i < size; i++) {
                String[] info = br.readLine().split(" ");
                int x = Integer.parseInt(info[0]);
                int y = Integer.parseInt(info[1]);
                nodeList.add(new Node(x, y));
            }

            for (int i = 0; i < size; i++) {
                for (int j = 0; j < size; j++) {
                    if (i != j) {
                        int distance = nodeList.get(i).distance(nodeList.get(j));
                        if (distance <= 1000) {
                            map[i][j] = true; // 연결 가능 여부만 확인
                        }
                    }
                }
            }

            for (int k = 0; k < size; k++) {
                for (int i = 0; i < size; i++) {
                    for (int j = 0; j < size; j++) {
                        if (map[i][k] && map[k][j]) {
                            map[i][j] = true;
                        }
                    }
                }
            }

            if (map[0][size - 1]) {
                bw.write("happy\n");
            } else {
                bw.write("sad\n");
            }
        }

        bw.flush();
        br.close();
        bw.close();
    }

    static class Node {
        int x, y;

        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public int distance(Node another) {
            return Math.abs(this.x - another.x) + Math.abs(this.y - another.y);
        }
    }
}