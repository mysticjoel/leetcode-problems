// Last updated: 7/24/2025, 12:03:16 AM
class Solution {
    public String reverseStr(String s, int k) {
        String ans = "";
        if (s.length() < k)
            return new StringBuilder(s).reverse().toString();
        else if (s.length() < 2 * k && s.length() >= k) {
            String f = s.substring(0, k);
            f = new StringBuilder(f).reverse().toString();
            String se = s.substring(k, s.length());
            return f + se;
        } else {

            int j = k;
            for (int i = 0; i < s.length(); i += k) {
                if (j > s.length()) {
                    ans += new StringBuilder(s.substring(i, s.length())).reverse().toString();
                    return ans;
                }
                String temp = new StringBuilder(s.substring(i, j)).reverse().toString();
                ans += temp;
                j += k;
                i += k;
                if (j > s.length()) {
                    ans += s.substring(i, s.length());
                    return ans;
                }
                ans += s.substring(i, j);
                j += k;

            }

        }
        return ans;
    }
}