class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst = s.split(' ')
        for i in range(len(lst)-1,-1,-1):
            if lst[i]:
                return len(lst[i])
        return 0
            