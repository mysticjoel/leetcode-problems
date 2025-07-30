// Last updated: 7/30/2025, 1:34:35 PM
class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        List<Integer> list = new ArrayList<>();
        int left = 0;
        int right = cols-1;
        int top = 0;
        int bottom = rows-1;
        int size = rows*cols;
        int i;
        while(list.size()<size){
            for(i=left;i<=right;i++){
                list.add(matrix[top][i]);
            }
            top++;
            for(i=top;i<=bottom;i++){
                list.add(matrix[i][right]);
            }
            right--;
            if(top<=bottom){
                for(i=right;i>=left;i--){
                    list.add(matrix[bottom][i]);
                }
                bottom--;
            }
            if(left<=right){
                for(i=bottom;i>=top;i--){
                    list.add(matrix[i][left]);
                }
                left++;
            }
        }
        return list;
    }
}