class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        string = ''
        for char in s:
            if char != '-':
                string += char.upper()
        
        mod = len(string) % k
        print(mod)
        res = ''

        if mod != 0:
            res += string[0:mod]
            res += '-'

        for i in range(mod, len(string), k):
            res += string[i: i+k]
            res += '-'
        return res[:-1]
