import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> pMap = new HashMap<>();
        for (String p: participant) {
            if (pMap.containsKey(p)) {
                int v = pMap.get(p);
                pMap.put(p, v + 1);
            } else {
                pMap.put(p, 1);
            }
        }
        
        for (String c: completion) {
            if (pMap.containsKey(c)) {
                int v = pMap.get(c);
                pMap.put(c, v - 1);

                if (v - 1 == 0) {
                    pMap.remove(c);
                }
            }
        }
        
        for (String key: pMap.keySet()) {
            return key;
        }
        
        return "";
    }
}