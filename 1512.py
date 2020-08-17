class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # O(n ^ 2) solution
        # count = 0                           # intialize the count
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):   # for all j > i
        #         if nums[j] == nums[i]:          # check the condition
        #             count += 1
        # return count

        # O(n) solution
        counts = [0] * 150                  # this is to count of elements
        good_pairs = 0
        for i in range(len(nums)):
            counts[nums[i]] += 1
        for i in range(len(counts)):
            # if the count is n then there will be n * (n - 1) / 2 good pairs
            good_pairs += ((counts[i] * (counts[i] - 1)) // 2)
        return good_pairs
