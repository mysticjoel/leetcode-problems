// Last updated: 8/10/2025, 1:55:58 AM
class Solution {
    public boolean isPowerOfTwo(int n) {
        if(n<0){
            return false;
        }
        for(int i=0;i<32;i++){
            if(n==Math.pow(2, i)) return true;
        }
        return false;
    }
}