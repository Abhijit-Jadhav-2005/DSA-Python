class Solution:
    def findLHS(self, nums):
        freq = {}

        # Count frequency of each number
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        ans = 0

        # Check consecutive numbers
        for num in freq:
            if num + 1 in freq:
                ans = max(ans, freq[num] + freq[num + 1])

        return ans