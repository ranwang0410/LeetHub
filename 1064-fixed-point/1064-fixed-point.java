class Solution {
    public int fixedPoint(int[] arr) {
       int start = 0, end = arr.length - 1, mid = 0, sim = -1;
        while(start <= end) {
            mid = (start + end) >>> 1;
            if(mid == arr[mid]) {
                sim = mid;
                end = mid - 1;
            }
            else if (mid > arr[mid]) start = mid + 1;
            else end = mid - 1;
        }
        return sim; 
    }
}