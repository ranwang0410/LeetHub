class Solution {
    public int[] shuffle(int[] nums, int n) {
        int[] ans = new int[nums.length];
        int i = 0;
        int j = n;
        int index = 0;
        while(i < n && j < nums.length){
            ans[index] = nums[i++];
            ans[index+1] = nums[j++];
            index += 2;
        }
        return ans;
    }
}