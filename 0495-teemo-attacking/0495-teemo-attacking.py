class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        tot=0
        for i in range(len(timeSeries)-1):
            if timeSeries[i+1]-timeSeries[i]>duration:
                tot+=duration
            else:
                tot+=timeSeries[i+1]-timeSeries[i]
        return tot+duration