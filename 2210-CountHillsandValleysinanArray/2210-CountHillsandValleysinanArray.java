// Last updated: 7/28/2025, 2:19:04 AM
class Solution {
    public int countHillValley(int[] nums) {
        int count = 0;
        int i = 1; 
        
        while (i < nums.length - 1) { 
            int j = i;
            while (j + 1 < nums.length && nums[j + 1] == nums[i]) {
                j++;
            }            
            if (i > 0 && j < nums.length - 1) {
                int left = i - 1;
                while (left > 0 && nums[left] == nums[i]) {
                    left--;
                }
                
                int right = j + 1;
                if (nums[left] < nums[i] && nums[right] < nums[i]) {
                    count++;
                } else if (nums[left] > nums[i] && nums[right] > nums[i]) {
                    count++;
                }
            }
            
            // Move to the next group of different values
            i = j + 1;
        }
        
        return count;
    }
}