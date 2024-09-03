class Solution {
    public int[] distributeCandies(int candies, int num_people) {
        int ans[] = new int[num_people];
        int i = 1;
        int idx = 0;
        while(candies>0){
            idx = (idx==num_people) ? 0 : idx;
            if(candies-i>=0){
                ans[idx++] += i;
                candies = candies-i;
                i++;
            }else{
                ans[idx++] += candies;
                break;
            }
        }
        return ans;
    }
}