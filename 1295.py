class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum([(len(str(el)) % 2 == 0) for el in nums])
