class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        max_freq = max(freq_map.values()) if freq_map else 0
        count_max_freq = sum(1 for freq in freq_map.values() if freq == max_freq)    
        return max_freq * count_max_freq
        