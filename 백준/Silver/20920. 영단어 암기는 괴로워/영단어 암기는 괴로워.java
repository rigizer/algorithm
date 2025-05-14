import java.io.*;
import java.util.*;

public class Main {
    static class Word implements Comparable<Word> {
        String word;
        int freq;

        public Word(String word, int freq) {
            this.word = word;
            this.freq = freq;
        }

        @Override
        public int compareTo(Word o) {
            if (this.freq != o.freq) return o.freq - this.freq;
            if (this.word.length() != o.word.length()) return o.word.length() - this.word.length();
            return this.word.compareTo(o.word);
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        Map<String, Integer> map = new HashMap<>();

        for (int i = 0; i < n; i++) {
            String word = br.readLine();
            if (word.length() < m) continue;

            map.put(word, map.getOrDefault(word, 0) + 1);
        }

        List<Word> wordList = new ArrayList<>();
        for (Map.Entry<String, Integer> entry: map.entrySet()) {
            wordList.add(new Word(entry.getKey(), entry.getValue()));
        }

        Collections.sort(wordList);

        StringBuilder sb = new StringBuilder();
        for (Word w: wordList) {
            sb.append(w.word).append("\n");
        }

        System.out.println(sb);
    }
}