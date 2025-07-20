// Last updated: 7/20/2025, 5:40:30 PM
class Solution {
    public int maxSubArray(int[] nums) {
        int currsum = 0;
        int maxsum = nums[0];
        int right = 0;

        while (right < nums.length) {
            currsum += nums[right];

            if (currsum > maxsum) {
                maxsum = currsum;
            }

            if (currsum < 0) {
                currsum = 0;
            }

            right++;
        }

        return maxsum;
    }
}
