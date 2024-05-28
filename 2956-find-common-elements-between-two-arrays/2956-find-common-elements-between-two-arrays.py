class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)
        
        
        common_elements = set_nums1.intersection(set_nums2)
        count_in_nums1 = sum(1 for num in nums1 if num in common_elements)
        count_in_nums2 = sum(1 for num in nums2 if num in common_elements)
        
        return [count_in_nums1, count_in_nums2]

        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        