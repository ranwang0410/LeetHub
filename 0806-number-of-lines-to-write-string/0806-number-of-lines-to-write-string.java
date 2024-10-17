class Solution {
    public int[] numberOfLines(int[] widths, String s) {
        int sum = 0, lines = 1;

        for(final char c : s.toCharArray()) {
            final int idx = c - 'a';

            if(sum + widths[idx] > 100) {
                lines++;
                sum = 0;
            }

            sum += widths[idx];
        }

        return new int[] { lines, sum };
    }
}