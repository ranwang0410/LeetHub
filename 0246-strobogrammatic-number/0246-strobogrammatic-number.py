class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        strobogram_map = {"0": "0",  "1" : "1", "8" : "8", "6": "9" , "9" : "6"}

        left = 0
        right = len(num) - 1

        while left <= right:
            if num[left] in strobogram_map:
                strobogram_value = strobogram_map[num[left]]
                if strobogram_value == num[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            else:
                return False
        return True
        