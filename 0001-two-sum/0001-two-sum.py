class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i in range(len(nums)):
            num2 = target - nums[i]
            if num2 in dic:
                return [dic[num2], i]
            else:
                dic[nums[i]] = i

        