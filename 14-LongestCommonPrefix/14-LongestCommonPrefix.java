// Last updated: 7/23/2025, 2:47:05 AM
class Solution {
    
    public String shortestString(String[] str){
        String shortest = str[0];
        for(String s : str){
            if(s.length() < shortest.length()){
                shortest = s;
            }
        }
        return shortest;
    }

    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) return "";
        String prefix = shortestString(strs);
        for (String s : strs) {
            while (!s.startsWith(prefix)) {
                prefix = prefix.substring(0, prefix.length() - 1);
                if (prefix.isEmpty()) return "";
            }
        }

        return prefix;
    }
}
