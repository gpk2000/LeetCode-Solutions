class Solution:
    def balancedStringSplit(self, s: str) -> int:
        amount = 0
        value = 0
        for ch in s:
            if ch == 'L':
                value -= 1
            else:
                value += 1
            if value == 0:
                amount += 1
        return amount
