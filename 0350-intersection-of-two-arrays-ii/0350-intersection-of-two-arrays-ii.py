class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        table = {}
        for number in nums1:
            table[number] = table.get(number, 0) + 1
        # Instantiate an empty list for result
        res = []
        for num in nums2:
            if num in table:
                if table[num] > 0:
                    res.append(num)
                    table[num] = table[num] - 1
        return res
        