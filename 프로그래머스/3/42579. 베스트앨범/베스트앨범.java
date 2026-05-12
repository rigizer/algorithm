import java.util.*;

class Solution {
    static class Song {
        int index;
        int play;

        Song(int index, int play) {
            this.index = index;
            this.play = play;
        }
    }

    public int[] solution(String[] genres, int[] plays) {
        Map<String, Integer> genrePlayMap = new HashMap<>();
        Map<String, List<Song>> genreSongMap = new HashMap<>();

        for (int i = 0; i < genres.length; i++) {
            genrePlayMap.put(
                genres[i],
                genrePlayMap.getOrDefault(genres[i], 0) + plays[i]
            );

            genreSongMap.putIfAbsent(genres[i], new ArrayList<>());
            genreSongMap.get(genres[i]).add(new Song(i, plays[i]));
        }

        List<String> genreList = new ArrayList<>(genrePlayMap.keySet());
        genreList.sort((a, b) -> genrePlayMap.get(b) - genrePlayMap.get(a));
        List<Integer> result = new ArrayList<>();
        for (String genre: genreList) {
            List<Song> songs = genreSongMap.get(genre);

            songs.sort((a, b) -> {
                if (a.play == b.play) {
                    return a.index - b.index;
                }

                return b.play - a.play;
            });

            result.add(songs.get(0).index);

            if (songs.size() > 1) {
                result.add(songs.get(1).index);
            }
        }

        int[] answer = new int[result.size()];

        for (int i = 0; i < result.size(); i++) {
            answer[i] = result.get(i);
        }

        return answer;
    }
}