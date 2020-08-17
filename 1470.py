class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffled_list = []                      # make a new list
        for i in range(n):
            shuffled_list.append(nums[i])       # add i th element
            shuffled_list.append(nums[i + n])   # add i + n th element
        return shuffled_list
