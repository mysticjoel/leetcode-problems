// Last updated: 7/29/2025, 5:24:54 PM
class Solution {
    public int mySqrt(int x) {
        int low = 0;
        int high = x;
        while (low<=high){
            int mid = (high+low)/2;
            long value = (long) mid*mid;
            if(value==x){
                return mid;
            }else if(value>x){
                high = mid-1;
            }else{
                low = mid+1;
            }
        }
        return high;
    }
}