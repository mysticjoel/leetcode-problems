// Last updated: 8/2/2025, 2:11:36 AM
import java.util.List;
import java.util.ArrayList;

class Solution {
    List<List<Integer>> pascal = new ArrayList<>();

    public List<Integer> setValue(int i){
        List<Integer> row = new ArrayList<>();
        for(int j=0;j<=i;j++){
            if(j==0||j==i){
                row.add(1);
            }else{
                int val = pascal.get(i-1).get(j-1) + pascal.get(i-1).get(j);
                row.add(val);
            }
        }
        return row;

    }
    public List<List<Integer>> generate(int numRows) {
        
        for(int i=0;i<numRows;i++){
            pascal.add(setValue(i));
        }
        return pascal;
    }
}