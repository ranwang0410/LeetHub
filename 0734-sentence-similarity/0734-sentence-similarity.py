class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2, similarPairs):
        """
        :type sentence1: List[str]
        :type sentence2: List[str]
        :type similarPairs: List[List[str]]
        :rtype: bool
        """
        if len(sentence1) != len(sentence2): return False
        for a, b in zip(sentence1, sentence2):
            if a == b:
                continue
            if [a, b] in similarPairs:
                continue
            if [b, a] in similarPairs:
                continue
            return False
        return True
            
        