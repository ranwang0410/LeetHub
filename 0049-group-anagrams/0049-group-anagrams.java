class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map= new HashMap<>();

        for(String word : strs){
            char[] ch= word.toCharArray(); 
            Arrays.sort(ch); 
            String anagram= new String(ch);
            if(!map.containsKey(anagram)){ 
                map.put(anagram, new ArrayList<>());
            }
            map.get(anagram).add(word); 
        }
        return new ArrayList<>(map.values());
    }
}