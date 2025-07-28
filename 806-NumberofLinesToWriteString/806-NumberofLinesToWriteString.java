// Last updated: 7/29/2025, 1:59:35 AM
class Solution {
    public int[] numberOfLines(int[] widths, String s) {
        HashMap<Character,Integer> map = new HashMap<>();
        int count = 0;
        for(int i=97;i<123;i++){
            Character c = (char) i;
            map.put(c,widths[count]);
            count++;
        }
        count = 0;
        int line = 1;
        for(char c: s.toCharArray()){
            if(count<=100){
                count+=map.get(c);
                if(count>100){
                    count=map.get(c);
                    line++;
                }
            }
        }
        int[] res = {line,count};
        return res;
    }
}