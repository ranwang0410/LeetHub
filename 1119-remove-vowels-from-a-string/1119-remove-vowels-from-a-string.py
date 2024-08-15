class Solution(object):
    def removeVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set('aeiou')
        result = ''.join([char for char in s if char not in vowels])
        return result
        