// Last updated: 7/15/2025, 3:05:53 AM
class Solution {
    public boolean checkPerfectNumber(int num) {
        if (num==1){
            return false;
        }
        int count = 0;
        int length = (int) Math.log10(num) + 10;
        int i = (int) Math.sqrt(num);
        while(i>1){
            if(num%i==0){
                count+=i;
                count += (num/i);
            }
            i--;
        }
        count++;
        if(count==num){
            return true;
        }else{
            return false;
        }
        
        
    }
}