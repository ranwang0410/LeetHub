class Solution {
    public boolean isNStraightHand(int[] hand, int groupSize) {
        if(hand.length%groupSize != 0)
        {
            return false;
        }
        int n = hand.length;
        Arrays.sort(hand);
        List<Integer> dups = new ArrayList<>();
        int ptr = 0;
        while(ptr < n)
        {
            int start = ptr;
            int prev = hand[start];
            int j = 1;
            start ++;
            while((j < n) && (j < groupSize) && (start < n))
            {
                if((prev + 1) == hand[start])
                {
                    prev = hand[start];
                    start ++;
                    j ++;
                }
                else if(prev == hand[start])
                {
                    dups.add(hand[start]);
                    start ++;
                }
                else 
                {
                    return false;
                }
            }
            if(j != groupSize)
            {
                return false;
            }
            ptr = start - dups.size();
            int temp = ptr;
            for(int k = 0; k < dups.size(); k ++, temp ++)
            {
                hand[temp] = dups.get(k);
            }
            dups = new ArrayList<>();
        }
        return true;
    }
}