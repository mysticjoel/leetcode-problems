// Last updated: 8/8/2025, 12:19:03 AM
class Solution {
    public int maxSum(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int num : nums) set.add(num);

        int result = 0;
        for (int num : set) {
            if (num > 0) result += num;
        }

        if (result == 0) {
            result = Collections.max(set);
        }

        return result;
    }
}