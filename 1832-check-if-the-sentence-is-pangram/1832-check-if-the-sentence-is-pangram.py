class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sen = set(sentence)
        return len(sen) == 26
        
        