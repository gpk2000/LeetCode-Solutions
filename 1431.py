class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)                  # get the max candies
        checkList = [False] * len(candies)          # initialize the check list
        for i in range(len(candies)):
            # check if the given condition is true
            checkList[i] = (candies[i] + extraCandies >= max_candies)
        return checkList
