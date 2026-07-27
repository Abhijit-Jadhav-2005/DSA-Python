class Solution:
    def findDisappearedNumbers(self, nums):
        # Mark the visited numbers
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])

        ans = []

        # Positive values indicate missing numbers
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i + 1)

        return ans