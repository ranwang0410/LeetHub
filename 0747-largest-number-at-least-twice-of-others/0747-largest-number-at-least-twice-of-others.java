class Solution {
    public int dominantIndex(int[] nums) {
        int max1;
        int max2;
        int max1i=0;
        max1=nums[0];
        for(int i=0;i<nums.length;i++){
            if(nums[i]>max1){
                max1=nums[i];
                max1i=i;
            }
        }
        if(nums[0]!=max1)
            max2=nums[0];
        else
            max2=nums[1];
        for(int b:nums){
            if(b>max2&&b<max1){
                max2=b;
            }
        }
        return ((max1>=(max2*2)?max1i:-1));
    }
}