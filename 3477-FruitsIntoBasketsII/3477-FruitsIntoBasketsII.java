// Last updated: 8/6/2025, 2:44:10 AM
class Solution {
    public int numOfUnplacedFruits(int[] fruits, int[] baskets) {
        int[] arr = new int[fruits.length];
        Arrays.fill(arr, 1);
        for(int i=0;i<fruits.length;i++){
            for(int j=0;j<baskets.length;j++){
                if((fruits[i]<=baskets[j]) && arr[j]==1){
                    arr[j] = 0;
                    break;
                }
            }
        }
        int sum = 0;
        for (int num : arr) {
            sum += num;
        }
        return sum;
    }
}