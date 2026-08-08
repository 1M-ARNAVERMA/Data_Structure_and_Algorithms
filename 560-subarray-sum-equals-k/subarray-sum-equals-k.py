class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        freq[0] = 1
        prefix_sum = 0
        ans = 0
        
        for num in nums:
            prefix_sum += num
            curSum = prefix_sum - k
            if curSum in freq:
                ans += freq[curSum]
            freq[prefix_sum] += 1
        return ans