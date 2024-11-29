class Solution {
    public int[][] allCellsDistOrder(int rows, int cols, int rCenter, int cCenter) {
        ArrayList<int[]> ans=new ArrayList<>(); 
        boolean[][] dp=new boolean[rows][cols];
        dp[rCenter][cCenter]=true;
        Queue<Integer> q=new LinkedList<Integer>();
        Queue<Integer> p=new LinkedList<Integer>();
        q.add(rCenter);
        p.add(cCenter);
        while(!q.isEmpty()){
            int size=q.size();
            for(int i=0;i<size;i++){
                int a=q.peek();
                int b=p.peek();
                q.poll();  
                p.poll();
                ans.add(new int[] {a,b});
                if(a-1>=0&&!dp[a-1][b]){
                    q.add(a-1);
                    p.add(b);
                    dp[a-1][b]=true;
                }
                if(b-1>=0&&!dp[a][b-1]){
                     q.add(a);
                    p.add(b-1);
                     dp[a][b-1]=true;
                }
                if(a+1<rows&&!dp[a+1][b]){
                    q.add(a+1);
                    p.add(b);
                     dp[a+1][b]=true;
                }
                if(b+1<cols && !dp[a][b+1]){
                     q.add(a);
                    p.add(b+1);
                     dp[a][b+1]=true;
                }
            }
        }
        return  ans.toArray(new int[0][0]);  
    }
}