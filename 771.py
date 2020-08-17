class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = 0
        for stones in S:
            if stones in J:
                jewels += 1
        return jewels
