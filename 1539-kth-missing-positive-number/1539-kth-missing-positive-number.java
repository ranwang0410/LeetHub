class Solution {
    public int findKthPositive(int[] arr, int k) {
        int n=arr.length;
        int prev=0,i=0;
        while(i<n){
            if(arr[i]==prev+1){
            i++;
            }
                
            else{
                k--;
                if(k==0) return prev+1;

            }
            prev++;
        }

        while(k>0){
            k--;
            prev++;
        }

        return prev;
    }
}