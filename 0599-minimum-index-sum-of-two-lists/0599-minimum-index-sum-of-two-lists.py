class Solution:
    def findRestaurant(self, list1, list2):
        index_map = {}

        # Store index of each string in list1
        for i in range(len(list1)):
            index_map[list1[i]] = i

        min_sum = float('inf')
        ans = []

        # Check common strings
        for j in range(len(list2)):
            if list2[j] in index_map:
                total = index_map[list2[j]] + j

                if total < min_sum:
                    min_sum = total
                    ans = [list2[j]]
                elif total == min_sum:
                    ans.append(list2[j])

        return ans