class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        operations = 0
        for num in nums:
            remainder = num % 3
            if remainder == 1:
                operations += 1
            elif remainder == 2:
                operations += 1
        return operations
