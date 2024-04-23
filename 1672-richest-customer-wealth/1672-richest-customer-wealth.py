class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        lst=[]
        
        for i in accounts:
            total=0
            for j in i:
                total=total+j
                lst.append(total)
        return max(lst)
        