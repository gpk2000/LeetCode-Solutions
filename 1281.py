class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        x = n
        product = 1
        while x:
            product *= x % 10
            x //= 10
        sumd = sum([int(ch) for ch in str(n)])
        return product - sumd
