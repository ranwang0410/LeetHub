class Solution {
    public boolean isHappy(int n) {
        Set<Long> seenNumbers = new HashSet<>();
        long m = n;
        while (m != 1 && !seenNumbers.contains(m)) {
            seenNumbers.add(m);
            long sum = 0;
            while (m > 0) {
                long digit = m % 10;
                sum += digit * digit;
                m /= 10;
            }
            m = sum;
        }        
        return m == 1;
        
    }
}