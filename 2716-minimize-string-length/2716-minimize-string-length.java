class Solution {
    public int minimizedStringLength(String s) {
        HashMap<Integer, Integer> map = new HashMap();
        for (int i = 0; i < s.length(); i++) {
            int charIndex = (int) (s.charAt(i));
            if (map.containsKey(charIndex)) {
                map.put(charIndex, map.get(charIndex) + 1);
            } else {
                map.put(charIndex, 1);

            }
        }
        String res = "";

        for (int i = 0; i < s.length(); i++) {
            int charIndex = (int) (s.charAt(i));

            if (map.get(charIndex) > 1) {
                res += s.charAt(i);
                map.put(charIndex, 0);
            } else if (map.get(charIndex) != 0) {
                res += s.charAt(i);
            }
        }
        return res.length();
        
    }
}