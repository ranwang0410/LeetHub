class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        if not diff :
            return 0
        l = len(nums)
        n = 0
        for i in range(l-2) :
            for j in range(i+1, l-1) :
                if nums[j] - nums[i] == diff :
                    for k in range(j+1, l) :
                        if nums[k] - nums[j] == diff :
                            n += 1
        return n
        