class Solution {
    public char slowestKey(int[] releaseTimes, String keysPressed) {
        int max = releaseTimes[0];
        char ch = keysPressed.charAt(0);

        for(int i=1;i<releaseTimes.length;i++) {
            if(max <= (releaseTimes[i] - releaseTimes[i-1])) {
                if(max == (releaseTimes[i] - releaseTimes[i-1])) {
                    if(Character.hashCode(ch) < Character.hashCode(keysPressed.charAt(i))) {
                        ch = keysPressed.charAt(i);
                    }
                } else {
                    ch = keysPressed.charAt(i);
                }
                max  = Math.max(max, (releaseTimes[i] - releaseTimes[i-1]));
            }
        }

        return ch;
    }
}