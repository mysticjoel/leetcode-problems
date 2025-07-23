// Last updated: 7/23/2025, 11:42:08 PM
class Solution {
    public String reverse(String s, int i, int j) {
        StringBuilder sb = new StringBuilder();
        for (int idx = j; idx >= i; idx--) {
            sb.append(s.charAt(idx));
        }
        return sb.toString();
    }

    public String reverseStr(String s, int k) {
        StringBuilder result = new StringBuilder();
        int n = s.length();

        for (int i = 0; i < n; i += 2 * k) {
            int end = Math.min(i + k - 1, n - 1);
            result.append(reverse(s, i, end));

            int nextStart = end + 1;
            int nextEnd = Math.min(i + 2 * k, n);
            if (nextStart < n) {
                result.append(s.substring(nextStart, nextEnd));
            }
        }

        return result.toString();
    }
}
