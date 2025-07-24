// Last updated: 7/24/2025, 5:58:19 PM
class Solution {
    public int maxFrequencyElements(int[] nums) {
        HashMap<Integer,Integer> hashmap = new HashMap<>();
        for(int i:nums){
            hashmap.put(i,hashmap.getOrDefault(i,0) + 1);
        }
        int count=0; 
        int maxval=Integer.MIN_VALUE;
        System.out.println("Frequencies: " + hashmap);
        for(int i:hashmap.values()){
            if(i>maxval){
                maxval=i;
            }
        }
        for(int i:hashmap.values()){
            if(i==maxval){
                count+=maxval;
            }
        }
        return count;
    }
}
