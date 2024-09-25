class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        char min=letters[0];
        for(char a:letters){
           if(a>target){
            min=a;
            break;
           }
        }
        return min;
    }
}