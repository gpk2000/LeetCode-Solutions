class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group_dict = dict()
        n = len(groupSizes)
        for i in range(n + 1):
            group_dict[i] = list()
        for i in range(n):
            group_dict[groupSizes[i]].append(i)
        groups = []
        for i in range(1, n + 1):
            for j in range(0, len(group_dict[i]), i):
                groups.append(group_dict[i][j: j + i])
        return groups
