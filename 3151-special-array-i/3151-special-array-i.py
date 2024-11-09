class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last_parity = nums[0] % 2 == 0 # True if even, False if Odd
        for i in range(1,len(nums)):
            parity = nums[i] % 2 == 0  # True if even, False if Odd
            if parity == last_parity: return False
            last_parity = not last_parity
        return True
        