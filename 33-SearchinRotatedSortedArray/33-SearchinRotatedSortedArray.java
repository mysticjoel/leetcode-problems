// Last updated: 7/31/2025, 6:01:07 PM
class Solution {
    public int search(int[] nums, int target) {
        int low = 0; int high = nums.length -1;
        while(low<=high){
            int mid = (low+high)/2;
            if(nums[mid]==target){return mid;}

            if(nums[mid]>=nums[low]){
                if(nums[low]<=target && nums[mid]>target){
                    high = mid -1;
                }else{
                    low = mid+1;
                }
            }
            else{
                if(nums[high]>=target && nums[mid]<target){
                    low = mid+1;
                }else{
                    high = mid-1;
                }
            }
        }
        return -1;
    }
}