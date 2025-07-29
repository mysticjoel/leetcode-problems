// Last updated: 7/29/2025, 5:11:12 PM
class Solution {
    public int binarysearch(int low,int high,int n){
        if(low>high){
            return high;
        }
        int mid = (high+low)/2;
        long value = ((long) mid * (mid + 1)) / 2;
        if(value==n){
            return mid;
        }
        else if(value>n){
            return binarysearch(low,mid-1,n);
        }else{
            return binarysearch(mid+1,high,n);
        }
    }
    public int arrangeCoins(int n) {
        return(binarysearch(0,n,n));
        
    }
}