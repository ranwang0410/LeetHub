class Solution {
    public boolean isIsomorphic(String s, String t) {
        int []map=new int [256];
        boolean []mapeed=new boolean [256];

        for(int i=0;i<s.length();i++)
        {
            if(map[s.charAt(i)]==0)
            {
                if(mapeed[t.charAt(i)])
                return false;
                map[s.charAt(i)]=t.charAt(i);
                mapeed[t.charAt(i)]=true;
            }
            else
            {
                if(map[s.charAt(i)]!=t.charAt(i))
                return false;
            }

        }

        return true;
    }
}