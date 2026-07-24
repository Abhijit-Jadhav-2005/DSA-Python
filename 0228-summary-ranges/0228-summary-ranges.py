class Solution:
    def summaryRanges(self, nums):
        result = []

        if not nums:
            return result

        start = nums[0]

        for i in range(1, len(nums)):
            # If numbers are not consecutive
            if nums[i] != nums[i - 1] + 1:
                if start == nums[i - 1]:
                    result.append(str(start))
                else:
                    result.append(str(start) + "->" + str(nums[i - 1]))

                # Start a new range
                start = nums[i]

        # Add the last range
        if start == nums[-1]:
            result.append(str(start))
        else:
            result.append(str(start) + "->" + str(nums[-1]))

        return result