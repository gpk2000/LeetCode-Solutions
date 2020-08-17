class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = [0] * 550
        valid_count = [0] * n
        for i in range(n):
            counts[nums[i]] += 1
        for i in range(n):
            valid_count[i] = sum(counts[: nums[i]])
        return valid_count
