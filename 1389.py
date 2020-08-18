class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target_arr = []
        for i in range(len(nums)):
            target_arr.insert(index[i], nums[i])
        return target_arr
