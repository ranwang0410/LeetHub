class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        return "".join([str(num) for num in sorted(nums, key=functools.cmp_to_key(lambda x,y: -1 if int(str(x)+str(y)) > int(str(y)+str(x)) else 1))]) if nums != [0]*len(nums) else "0"