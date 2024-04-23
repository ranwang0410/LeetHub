class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        count = 0
        lst = []
        for i in candies:
            lst.append(i+extraCandies >= max(candies))
        return lst   
            
        
        
        