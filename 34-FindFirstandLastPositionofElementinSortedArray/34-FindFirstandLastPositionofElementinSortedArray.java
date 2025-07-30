// Last updated: 7/30/2025, 12:28:28 PM
class Solution {
    public int binsearch(int low,int high,int target,int[] nums,boolean check){
        if(low>high){
            return -1;
        }
        int mid = (low+high)/2;
        if(nums[mid]==target){
            if(check){
                int next = binsearch(mid+1,nums.length-1,target,nums,true);
                return (next == -1) ? mid : next;
            }else{
                int prev = binsearch(0,mid-1,target,nums,false);
                return (prev==-1) ? mid:prev;
            }
        }else if(target>nums[mid]){
            return binsearch(mid+1,high,target,nums,check);
        }else{
            return binsearch(low,mid-1,target,nums,check);
        }
    }
    public int[] searchRange(int[] nums, int target) {
        int[] res = {-1,-1};
        //int left = binsearch(0,val-1,target,nums,false);
        int left = binsearch(0,nums.length - 1,target,nums,false);
        if(left==-1) return res;
        int right = binsearch(0,nums.length - 1,target,nums,true);
        res[0] = left;
        res[1] = right;
        return res;
    }
}