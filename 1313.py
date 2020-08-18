class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decompressed_list = []
        for i in range(0, len(nums), 2):
            decompressed_list += [nums[i + 1]] * nums[i]
        return decompressed_list
