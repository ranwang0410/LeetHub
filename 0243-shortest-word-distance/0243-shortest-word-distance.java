class Solution {
    public int shortestDistance(String[] wordsDict, String word1, String word2) {
        int word1Pos = -1; int word2Pos = -1; int distance = Integer.MAX_VALUE;
        for(int i=0; i<wordsDict.length; i++) {
            String word = wordsDict[i];
            if(word.equals(word1))  word1Pos = i;
            if(word.equals(word2))  word2Pos = i;
            if(word1Pos > -1 && word2Pos > -1) {
                distance = Math.min(distance, Math.abs(word1Pos - word2Pos));
            }
        }
        return distance;
    }
}