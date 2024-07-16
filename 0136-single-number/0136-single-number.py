class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] =1
            else:
                d[nums[i]] += 1

        for keys, value in d.items():
            if d[keys] == 1:
                return keys
        