class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled_string = [None] * len(s)
        for i in range(len(indices)):
            shuffled_string[indices[i]] = s[i]
        return ''.join([ch for ch in shuffled_string])
