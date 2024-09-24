class Solution {
    public List<String> generatePossibleNextMoves(String currentState) {
        List<String> toReturn = new ArrayList<>();
        StringBuilder objStringBuilder;
       for(int i = 1; i < currentState.length(); i++){
            if(currentState.charAt(i-1) == '+' && currentState.charAt(i) == '+'){
                objStringBuilder = new StringBuilder();
                objStringBuilder.append(currentState.substring(0, i-1));
                objStringBuilder.append("--");
                if(i + 1 < currentState.length()){ 
                    objStringBuilder.append(currentState.substring(i+1, currentState.length()));
                }
                toReturn.add(objStringBuilder.toString());
            }
       } 
       return toReturn;
    }
}