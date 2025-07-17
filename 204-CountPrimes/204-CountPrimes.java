// Last updated: 7/18/2025, 1:44:47 AM
import java.util.Arrays;

class Solution {
    public int sum(int [] prime){
        int count = 0;
        for(int val: prime){
            count += val;
        }
        return count;
    }
    public int countPrimes(int n) {
        int[] prime = new int[n+1];
        Arrays.fill(prime,1);
        prime[0]=0;
        prime[prime.length - 1] = 0;
        if (n>0) prime[1] = 0;
        for(int i=2;i<Math.sqrt(n);i++){
            if(prime[i]==0){
                continue;
            }
            for(int j=i;j<n;j++){
                if(i*j>=n){
                    break;
                }
                int val = i*j;
                //System.out.print(val);
                prime[val] = 0;
            }
        }
        return sum(prime);
    }
}