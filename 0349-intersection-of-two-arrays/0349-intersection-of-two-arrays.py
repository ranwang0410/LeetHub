class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1HashMap = {}
        result = []
        for n,i in enumerate(nums1):
            nums1HashMap[i] = n
        print(nums1HashMap)
        for i in nums2:
            if i in nums1HashMap:
                if i not in result:
                    result.append(i)
        return result
        