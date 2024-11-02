class Solution {
    public int diagonalSum(int[][] mat) {
        int sum=0;
        int n=mat.length;
        for(int r=0,c=0;r<n;r++,c++){
            sum+=mat[r][c];
        }
        for(int r=0,c=n-1;r<n;r++,c--){
            if(r!=c)
            sum+=mat[r][c];
        }
        return sum;
    }
}