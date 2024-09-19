class Solution {
    public int reverse(int x) {
        int num = Math.abs(x);
        long rev = 0;
        int obt;
        while (num > 0) {
            obt = num % 10;
            num = num / 10;
            rev = (rev * 10) + obt;
        }
        if (rev >= Integer.MIN_VALUE && rev <= Integer.MAX_VALUE) {
            return x < 0 ? (int)(-rev) : (int)rev;
        } else {
            return 0;
        }
    }
}