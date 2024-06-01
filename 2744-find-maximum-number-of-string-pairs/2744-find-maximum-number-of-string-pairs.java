class Solution {
    public int maximumNumberOfStringPairs(String[] words) {
        int maxPairs = 0;
        
        Set<String> wordSet = new HashSet<>();
        
        for(String word : words) {
            StringBuilder sb = new StringBuilder(word);
            String reversedWord = sb.reverse().toString();
            
            if(wordSet.contains(reversedWord)) {
                maxPairs++;
            }
            
            wordSet.add(word);
        }
        
        return maxPairs;
    }
}