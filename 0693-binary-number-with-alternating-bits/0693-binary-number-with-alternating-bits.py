class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        d = bin(n)[2:]
        s = str(d)
        u = s[::2]
        g = s[1::2]
        if(n==1 or n==0):
            return True
        if(set(u)== {'0'} and set(g)=={'1'}) or (set(u)== {'1'} and set(g)=={'0'}) :
            return True
        else:
            return False