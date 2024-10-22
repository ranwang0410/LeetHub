class Solution(object):
    def largestUniqueNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums, reverse=True)
        prev = None
        largest = -1
        i =0
        while i <= len(nums)+1:
            if i == len(nums)-1:
                if nums[i] != prev:
                    largest = max(nums[i], largest)
                    print(prev, nums[i], largest)
                break

            if nums[i] != prev and nums[i]!= nums[i+1]:
                largest = max(nums[i], largest)
            prev = nums[i]
            i+=1
        return largest