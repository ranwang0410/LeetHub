class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        n = len(words)
        cnt = 0
        seen = {}
        for i in range(n):        
            if seen.get(words[i][::-1]):
                seen[words[i][::-1]] += 1
            else:
                seen[words[i]] = 1
        for key,val in seen.items():
            if val>1:
                cnt += val-1
        return cnt
        """
        :type words: List[str]
        :rtype: int
        """
        