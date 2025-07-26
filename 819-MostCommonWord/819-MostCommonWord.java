// Last updated: 7/27/2025, 4:21:04 AM
class Solution {
    public boolean check(String str,String[] banned){
        for(int i=0;i<banned.length;i++){
            if (banned[i].equals(str))return true;
        }
        return false;
    }
    public String mostCommonWord(String paragraph, String[] banned) {
        HashMap<String,Integer> map = new HashMap<>();
        paragraph = paragraph.toLowerCase().replaceAll("[^a-zA-Z ]", " ");;
        String words[] = paragraph.split(" ");
        for (String word : words) {
            if (word.isEmpty()) {
                continue;
            }
            if (!check(word, banned)) {
                map.put(word, map.getOrDefault(word, 0) + 1);
            }
        }                         
        int larg = Integer.MIN_VALUE;
        Integer value;
        String key=" ";
        for(Map.Entry<String, Integer> entry : map.entrySet()){
            value = entry.getValue();
            if (value>larg){
                larg = value;
                key = entry.getKey();
            } 
        }
        return key;
    }
}