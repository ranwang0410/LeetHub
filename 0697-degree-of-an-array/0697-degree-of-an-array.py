class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        idx = {}
        
        for i, num in enumerate(nums):
            if num not in count:
                count[num]=1
                idx[num] = [i, i]
            else:
                count[num]+=1
                idx[num][1] = i 
                
        
        deg = max(count.values())
        
        
        listOfKeys = [key for (key, value) in count.items() if value==deg]
        
        ln=len(nums)

        for key in listOfKeys:
            lb=idx[key][0]
            ub=idx[key][1]
            ln = min(ln, ub-lb+1)
            
        return ln
        