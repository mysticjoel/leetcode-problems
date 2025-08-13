// Last updated: 8/14/2025, 3:41:50 AM
class Solution {
    public boolean isPowerOfThree(int n) {
        if(n<1) return false;
        for(int i=0;i<32;i++){
            if(Math.pow(3,i)==n) return true;
        }
        return false;
    }
}