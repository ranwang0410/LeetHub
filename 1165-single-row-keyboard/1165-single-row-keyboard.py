class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        idx=0
        sum=0
        for i in word:
            id=keyboard.index(i)
            sum=sum+abs(id-idx)
            idx=id
        return sum
        