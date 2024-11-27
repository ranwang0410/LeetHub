class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        stack = []      
        for num in arr:
            minVal, maxVal = num, num
            while stack and stack[-1][1] > minVal:
                minVal, maxVal = min(minVal, stack[-1][0]), max(maxVal, stack[-1][1])
                stack.pop()
            stack.append((minVal, maxVal))

        return len(stack)
        