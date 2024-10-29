class Solution {
    public int subsetXORSum(int[] nums) {
         int ans = 0;
        int n = nums.length;
        
        for (int el : nums) {
            ans |= el;
        }
        
        return ans * (1 << (n - 1));
    }
}