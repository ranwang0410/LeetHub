class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        w=[]
        c=0
        for i in range(left,right+1,1):
            c=0
            s=str(i)
            for j in s:
                j=int(j)
                if j!=0 and i%j==0:
                    c+=1
            if c==len(s):
                w.append(i)
        return w