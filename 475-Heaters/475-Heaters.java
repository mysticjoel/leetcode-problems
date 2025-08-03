// Last updated: 8/3/2025, 11:56:59 PM
class Solution {
    public int findRadius(int[] houses, int[] heaters) {
        
        Arrays.sort(heaters);

        int ans = 0;

        for(int house : houses)
        {
            ans = Math.max(ans, closestHeaterDistance(house, heaters));
        }

        return ans;
    }

    static int closestHeaterDistance(int house, int[] heaters)
    {
        int low = 0;
        int high = heaters.length - 1;

        int min_dist = Integer.MAX_VALUE;

        while(low <= high)
        {
            int mid = low + (high - low)/2;

            min_dist = Math.min(min_dist, Math.abs(house - heaters[mid]));

            if(heaters[mid] == house) 
                return 0;

            if(heaters[mid] > house) 
                high = mid - 1;

            else 
                low = mid + 1;
        }

        return min_dist;
    }
}