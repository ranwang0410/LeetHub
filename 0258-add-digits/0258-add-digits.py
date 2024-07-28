class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            num=str(num)
            num=[int(j) for j in num]    
            num=sum(num)
        return num
        