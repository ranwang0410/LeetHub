class Solution {
    public boolean canFormArray(int[] arr, int[][] pieces) {
        String s = "";
    Map<Integer, int[]> myMap = new HashMap<Integer, int[]>();

    for (int i = 0 ; i < pieces.length ; i++){
        myMap.put(pieces[i][0], pieces[i]);
    }

    for (int i = 0 ; i < arr.length ; i++){
        if (myMap.containsKey(arr[i])){
            s = s + ", " + Arrays.toString(myMap.get(arr[i]));
            i = i + (myMap.get(arr[i]).length) - 1;
        }
        else return false;
    }

    s = "[" + s.replaceAll("\\[|\\]", "").replaceAll("^, ", "") + "]";
    return Arrays.toString(arr).equals(s);    
    }
}