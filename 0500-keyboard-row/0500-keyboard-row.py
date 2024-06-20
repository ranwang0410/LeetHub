class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        first = "qwertyuiopQWERTYUIOP"
        second = "asdfghjklASDFGHJKL"
        third = "zxcvbnmZXCVBNM"
        res = []
        f = ''
        s = ''
        t = ''
        for i in words:
            for j in i:
                if j in first:
                    f += j
                elif j in second:
                    s += j
                elif j in third:
                    t += j
            if f == i or s == i or t == i:
                res.append(i)
            f,s,t = '','',''
        return res  
        