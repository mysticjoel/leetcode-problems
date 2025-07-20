// Last updated: 7/20/2025, 4:36:04 PM
class Solution {
    public void nextPermutation(int[] n) {
        int i;
        for(i=n.length-1;i>=1;i--)
        {
            if(n[i]<=n[i-1])
            continue;
            break;
        }
        
        if(i==0){
        Arrays.sort(n,0,n.length);
        return;}
        i-=1;
        int min=n[i+1],m=i+1;
        for(int j=i+2;j<n.length;j++)
        {
            if(n[j]<min&&n[j]>n[i]){
            min=n[j];
            m=j;}
        }
        int temp=min;
        min=n[i];
        n[i]=temp;
        n[m]=min;
        Arrays.sort(n,i+1,n.length);
    }
}