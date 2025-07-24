// Last updated: 7/24/2025, 6:53:41 PM
class Solution {
    public String frequencySort(String s) {
        HashMap<String,Integer> map= new HashMap<>();
        char[] charArray = s.toCharArray();
        StringBuilder sb = new StringBuilder();
        for(char word:charArray){
            String key = String.valueOf(word);
            map.put(key,map.getOrDefault(key,0)+1);
        }
        int maxVal = Integer.MIN_VALUE;
        String maxKey = null;
        while(map.size()>0){
            for (Map.Entry<String, Integer> entry : map.entrySet()) {
                int value = entry.getValue();
                if (value > maxVal) {
                    maxVal = value;
                    maxKey = entry.getKey();
                }
            }
            for(int i=0;i<maxVal;i++){
                sb.append(maxKey);
            }
            map.remove(maxKey);
            maxVal = Integer.MIN_VALUE;
        }
        return sb.toString();
    }
}